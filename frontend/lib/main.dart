import 'package:flutter/material.dart';
import 'package:frontend/src/services/api_contact.dart';

void main() {
  runApp(const WiFiFinderApp());
}

class WiFiFinderApp extends StatelessWidget {
  const WiFiFinderApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'WiFi Finder', home: const HomeScreen());
  }
}

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => HomeScreenState();
}

class HomeScreenState extends State<HomeScreen> {
  String message = "";
  bool isTalking = false;
  final APIContact api = APIContact();

  Future<void> pingBackend() async {
    setState(() {
      message = "Attempting to ping server";
      isTalking = true;
    });
    final backend_message = await api.checkAPIStatus();
    print(backend_message);
    setState(() {
      message = backend_message;
      isTalking = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Wifi Finder Basic')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              SizedBox(
                height: 20,
                child: Text(message, textAlign: TextAlign.center),
              ),
              ElevatedButton(
                onPressed: isTalking ? null : pingBackend,
                child: const Text('Check API status'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
