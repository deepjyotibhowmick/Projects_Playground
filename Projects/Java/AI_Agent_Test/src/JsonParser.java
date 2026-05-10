public class JsonParser {
    // Very small, targeted JSON helpers for the OpenWeatherMap response shape.

    // Extract a string value for a top-level key, e.g. "name":"London"
    public static String extractTopLevelString(String json, String key) {
        String q = "\"" + key + "\"";
        int idx = json.indexOf(q);
        if (idx == -1) return null;
        int colon = json.indexOf(':', idx + q.length());
        if (colon == -1) return null;
        int quoteStart = json.indexOf('"', colon + 1);
        if (quoteStart == -1) return null;
        int quoteEnd = json.indexOf('"', quoteStart + 1);
        if (quoteEnd == -1) return null;
        return json.substring(quoteStart + 1, quoteEnd);
    }

    // Extract a nested string like weather[0].description
    public static String extractWeatherDescription(String json) {
        String arrKey = "\"weather\"";
        int idx = json.indexOf(arrKey);
        if (idx == -1) return null;
        int bracketStart = json.indexOf('[', idx);
        if (bracketStart == -1) return null;
        int descIdx = json.indexOf("\"description\"", bracketStart);
        if (descIdx == -1) return null;
        int colon = json.indexOf(':', descIdx + 13);
        if (colon == -1) return null;
        int quoteStart = json.indexOf('"', colon + 1);
        if (quoteStart == -1) return null;
        int quoteEnd = json.indexOf('"', quoteStart + 1);
        if (quoteEnd == -1) return null;
        return json.substring(quoteStart + 1, quoteEnd);
    }

    // Extract number value for a path like main.temp or wind.speed
    public static Double extractNumber(String json, String path) {
        // Supports one-level like "main" -> "temp" as "main.temp"
        String[] parts = path.split("\\.");
        if (parts.length != 2) return null;
        String objKey = "\"" + parts[0] + "\"";
        int objIdx = json.indexOf(objKey);
        if (objIdx == -1) return null;
        int braceStart = json.indexOf('{', objIdx);
        if (braceStart == -1) return null;
        int keyIdx = json.indexOf('"' + parts[1] + '"', braceStart);
        if (keyIdx == -1) return null;
        int colon = json.indexOf(':', keyIdx + parts[1].length() + 2);
        if (colon == -1) return null;
        // extract until comma or closing brace
        int end = json.indexOf(',', colon);
        int braceEnd = json.indexOf('}', colon);
        if (end == -1 || (braceEnd != -1 && braceEnd < end)) end = braceEnd;
        if (end == -1) end = json.length();
        String numStr = json.substring(colon + 1, end).trim();
        try {
            return Double.parseDouble(numStr);
        } catch (NumberFormatException e) {
            return null;
        }
    }
}
