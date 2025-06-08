import 'package:http/http.dart' as http;

class APIContact {
  final String base = "http://192.168.0.71:8000";

  Future<String> checkAPIStatus() async {
    try {
      final response = await http
          .get(Uri.parse(base))
          .timeout(const Duration(seconds: 5));
      if (response.statusCode == 204) {
        return "API is online";
      } else {
        return "ERROR: API is offline";
      }
    } catch (e) {
      return "ERROR: API is offline";
    }
  }
}
