import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_stripe/flutter_stripe.dart';
import 'package:payment_app/core/config/app_config.dart';
import 'package:payment_app/core/theme/app_theme.dart';
import 'package:payment_app/features/auth/providers/auth_provider.dart';
import 'package:payment_app/features/auth/screens/login_screen.dart';
import 'package:payment_app/features/auth/screens/register_screen.dart';
import 'package:payment_app/features/navigation/screens/main_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialize Firebase
  await Firebase.initializeApp(
    options: const FirebaseOptions(
      apiKey: AppConfig.firebaseApiKey,
      projectId: AppConfig.firebaseProjectId,
      messagingSenderId: AppConfig.firebaseMessagingSenderId,
      appId: AppConfig.firebaseAppId,
    ),
  );

  // Initialize Stripe
  Stripe.publishableKey = AppConfig.stripePublishableKey;
  await Stripe.instance.applySettings();

  runApp(
    const ProviderScope(
      child: PaymentApp(),
    ),
  );
}

class PaymentApp extends ConsumerWidget {
  const PaymentApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final authState = ref.watch(authStateProvider);

    return MaterialApp(
      title: AppConfig.appName,
      theme: AppTheme.lightTheme,
      home: authState.when(
        data: (user) {
          if (user == null) {
            return const LoginScreen();
          }
          return const MainScreen();
        },
        loading: () => const SplashScreen(),
        error: (error, stackTrace) => const LoginScreen(),
      ),
      routes: {
        '/login': (context) => const LoginScreen(),
        '/register': (context) => const RegisterScreen(),
        '/main': (context) => const MainScreen(),
      },
      debugShowCheckedModeBanner: false,
    );
  }
}

class SplashScreen extends StatelessWidget {
  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(
        child: CircularProgressIndicator(),
      ),
    );
  }
}
