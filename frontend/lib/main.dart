import 'package:flutter/material.dart';
import 'package:frontend/src/services/ping.dart';

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

  Ping api = APIPing();
  Ping database = DatabasePing();

  Future<void> pingBackend(int option) async {
    setState(() {message = "Attempting to ping"; isTalking = true;});
    String backend_message = "";
    switch (option) {
      case 0: backend_message = await api.checkStatus();
      case 1: backend_message = await database.checkStatus();
    }
    setState(() {message = backend_message; isTalking = false;});
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
                onPressed: isTalking ? null : () => pingBackend(0),
                child: const Text('Check API status'),
              ),
              ElevatedButton(
                onPressed: isTalking ? null : () => pingBackend(1),
                child: const Text('Check Database status'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
