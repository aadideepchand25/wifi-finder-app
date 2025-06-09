import 'package:http/http.dart' as http;

const String base = String.fromEnvironment('apiuri');

abstract class Ping {
  final String endpoint;

  Ping(this.endpoint);

  String returnMessage(bool status);

  Future<String> checkStatus() async {
    try {
      final response = await http
          .get(Uri.parse(base + endpoint))
          .timeout(const Duration(seconds: 5));
      if (response.statusCode == 204) {
        return returnMessage(true);
      } else {
        return returnMessage(false);
      }
    } catch (e) {
      return returnMessage(false);
    }
  }
}

class APIPing extends Ping {
  APIPing() : super("/");
  @override
  String returnMessage(bool status) {
    return status ? "API is online" : "ERROR: API is offline";
  }
}

class DatabasePing extends Ping {
  DatabasePing() : super("/status");
  @override
  String returnMessage(bool status) {
    return status ? "Database is online" : "ERROR: Database is offline";
  }
}
