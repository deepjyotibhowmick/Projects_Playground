public class WeatherInfo {
    public final String city;
    public final String country;
    public final double temperature;
    public final String unitSymbol;
    public final String description;
    public final int humidity;
    public final double windSpeed;
    public final String rawJson;

    public WeatherInfo(String city, String country, double temperature, String unitSymbol,
                       String description, int humidity, double windSpeed, String rawJson) {
        this.city = city;
        this.country = country;
        this.temperature = temperature;
        this.unitSymbol = unitSymbol;
        this.description = description;
        this.humidity = humidity;
        this.windSpeed = windSpeed;
        this.rawJson = rawJson;
    }

    public String toDisplayString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Weather for ").append(city);
        if (country != null && !country.isEmpty()) sb.append(", ").append(country);
        sb.append("\n");
        sb.append("  Description: ").append(description == null ? "N/A" : description).append("\n");
        sb.append("  Temperature: ").append(String.format("%.2f", temperature)).append(unitSymbol).append("\n");
        sb.append("  Humidity: ").append(humidity).append("%\n");
        sb.append("  Wind speed: ").append(String.format("%.2f", windSpeed)).append(" m/s\n");
        return sb.toString();
    }
}
