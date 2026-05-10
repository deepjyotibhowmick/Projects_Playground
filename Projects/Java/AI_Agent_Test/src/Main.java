public class Main {
    public static void main(String[] args) {
        java.io.Console console = System.console();
        java.util.Scanner scanner = null;
        boolean useScanner = false;
        if (console == null) {
            // IDEs often don't provide a Console; fall back to Scanner
            scanner = new java.util.Scanner(System.in, "UTF-8");
            useScanner = true;
        }

        printHeader();

        while (true) {
            String city = prompt("Enter city (or 'quit' to exit): ", console, scanner, useScanner);
            if (city == null) break;
            city = city.trim();
            if (city.equalsIgnoreCase("quit") || city.equalsIgnoreCase("exit")) break;
            if (city.isEmpty()) {
                System.out.println("City cannot be empty. Try again.");
                continue;
            }

            String unitStr = prompt("Choose unit - (C)elsius, (F)ahrenheit, (K) Kelvin [default C]: ", console, scanner, useScanner);
            char unit = 'C';
            if (unitStr != null && !unitStr.trim().isEmpty()) {
                unit = Character.toUpperCase(unitStr.trim().charAt(0));
                if (unit != 'C' && unit != 'F' && unit != 'K') {
                    System.out.println("Invalid unit, using Celsius.");
                    unit = 'C';
                }
            }

            try {
                String json = WeatherClient.fetchWeather(city, unit);
                WeatherInfo info = parseWeather(json, unit);
                if (info != null) {
                    System.out.println(info.toDisplayString());
                } else {
                    System.out.println("Failed to parse weather response. Raw response:\n" + json);
                }
            } catch (Exception e) {
                System.out.println("Error fetching weather: " + e.getMessage());
            }

            System.out.println("--- Done.\n");
        }

        if (scanner != null) scanner.close();
        System.out.println("Goodbye.");
    }

    // Helper to prompt using Console if available otherwise Scanner
    private static String prompt(String message, java.io.Console console, java.util.Scanner scanner, boolean useScanner) {
        if (console != null) {
            return console.readLine(message);
        } else {
            System.out.print(message);
            if (scanner.hasNextLine()) return scanner.nextLine();
            return null;
        }
    }

    private static void printHeader() {
        System.out.println("Simple Weather Forecast (Console)");
        System.out.println("Provide a city name (e.g. London or \"New York\") and choose units.");
        System.out.println("If you haven't set an API key in WeatherClient, the app runs in demo mode.");
        System.out.println();
    }

    private static WeatherInfo parseWeather(String json, char unit) {
        if (json == null || json.isEmpty()) return null;
        String city = JsonParser.extractTopLevelString(json, "name");
        String country = JsonParser.extractTopLevelString(json, "country");
        if (country == null) {
            // country usually is under sys.country
            country = null;
            int sysIdx = json.indexOf("\"sys\"");
            if (sysIdx != -1) {
                int countryIdx = json.indexOf("\"country\"", sysIdx);
                if (countryIdx != -1) {
                    country = JsonParser.extractTopLevelString(json.substring(sysIdx, Math.min(json.length(), sysIdx + 300)), "country");
                }
            }
        }
        String description = JsonParser.extractWeatherDescription(json);
        Double temp = JsonParser.extractNumber(json, "main.temp");
        Double humidityD = JsonParser.extractNumber(json, "main.humidity");
        Double windSpeed = JsonParser.extractNumber(json, "wind.speed");

        int humidity = humidityD == null ? 0 : humidityD.intValue();
        double t = temp == null ? 0.0 : temp.doubleValue();
        String symbol = unitSymbol(unit);

        return new WeatherInfo(city == null ? "Unknown" : city,
                country == null ? "" : country,
                t,
                symbol,
                description == null ? "N/A" : description,
                humidity,
                windSpeed == null ? 0.0 : windSpeed.doubleValue(),
                json);
    }

    private static String unitSymbol(char unit) {
        if (unit == 'F') return " °F";
        if (unit == 'K') return " K";
        return " °C";
    }
}