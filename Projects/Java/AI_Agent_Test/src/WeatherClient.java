import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URLEncoder;
import java.net.URL;

public class WeatherClient {
    // Set your API key here. Leave as placeholder to enable demo mode.
    private static final String API_KEY = "4572f8cea58e0ac000da9509d9620f40";
    private static final int CONNECT_TIMEOUT_MS = 5000;
    private static final int READ_TIMEOUT_MS = 5000;

    public static String fetchWeather(String city, char unit) throws IOException {
        if (API_KEY == null || API_KEY.isEmpty() || API_KEY.equals("4572f8cea58e0ac000da9509d9620f40")) {
            // Demo JSON (simplified) - mimics OpenWeatherMap current weather response
            return demoJson(city);
        }
        String url = buildUrl(city, unit);
        HttpURLConnection conn = null;
        try {
            URL u = new URL(url);
            conn = (HttpURLConnection) u.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(CONNECT_TIMEOUT_MS);
            conn.setReadTimeout(READ_TIMEOUT_MS);
            int status = conn.getResponseCode();
            InputStream is = (status >= 200 && status < 300) ? conn.getInputStream() : conn.getErrorStream();
            String body = readStream(is);
            if (status < 200 || status >= 300) {
                throw new IOException("HTTP " + status + ": " + body);
            }
            return body;
        } finally {
            if (conn != null) conn.disconnect();
        }
    }

    private static String buildUrl(String city, char unit) throws IOException {
        String base = "https://api.openweathermap.org/data/2.5/weather";
        String unitsParam = "";
        if (unit == 'C' || unit == 'c') unitsParam = "&units=metric";
        if (unit == 'F' || unit == 'f') unitsParam = "&units=imperial";
        String q = URLEncoder.encode(city, "UTF-8");
        return base + "?q=" + q + unitsParam + "&appid=" + URLEncoder.encode(API_KEY, "UTF-8");
    }

    private static String readStream(InputStream is) throws IOException {
        if (is == null) return "";
        BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append('\n');
        }
        return sb.toString();
    }

    private static String demoJson(String city) {
        // Minimal response. Values chosen arbitrarily for demo.
        return "{\n" +
                "  \"name\": \"" + escapeJson(city) + "\",\n" +
                "  \"sys\": { \"country\": \"US\" },\n" +
                "  \"weather\": [ { \"description\": \"clear sky\" } ],\n" +
                "  \"main\": { \"temp\": 18.5, \"humidity\": 45 },\n" +
                "  \"wind\": { \"speed\": 3.5 }\n" +
                "}\n";
    }

    private static String escapeJson(String s) {
        return s.replace("\\", "\\\\").replace("\"", "\\\"");
    }
}
