class AppConfig {
  // API Keys and Endpoints
  static const String stripePublishableKey =
      'pk_test_51RN5OcQUP0FwU2NWRpgRs5E1vhTNeOwE7vpKDiLsK2BUYS98UPVd5npC0iwx8HDK5Bnpz55UEstVs8rreAM1eucX00tB49X1tN';
  static const String stripeSecretKey =
      'sk_test_51RN5OcQUP0FwU2NWxJlpw1PDfmYJrmskZ69vhAnChyP8RXjFpUQVcSFeGCAL4969dOrSxaZBqQLHeXIyHSlcHmE200xmghdsGI';

  // Firebase Configuration
  static const String firebaseApiKey =
      'AIzaSyDwq6v83hsBp6XCvSrxItQ3lE8xGddg0ro';
  static const String firebaseProjectId = 'payment-app-37261';
  static const String firebaseMessagingSenderId = '475444096860	';
  static const String firebaseAppId =
      '1:475444096860:android:ffde8290faeece625c5b99';

  // App Settings
  static const String appName = 'Payment App';
  static const String appVersion = '1.0.0';
  static const int apiTimeout = 30000; // 30 seconds
  static const int maxRetryAttempts = 3;

  // Cache Settings
  static const int cacheDuration = 7; // days
  static const String cacheBoxName = 'payment_app_cache';

  // Payment Settings
  static const String defaultCurrency = 'USD';
  static const List<String> supportedCurrencies = ['USD', 'EUR', 'GBP'];
  static const double minimumPaymentAmount = 1.0;
  static const double maximumPaymentAmount = 10000.0;

  // Error Messages
  static const String genericErrorMessage =
      'Something went wrong. Please try again.';
  static const String networkErrorMessage =
      'Please check your internet connection.';
  static const String paymentErrorMessage = 'Payment failed. Please try again.';

  // Success Messages
  static const String paymentSuccessMessage = 'Payment successful!';
  static const String profileUpdateSuccessMessage =
      'Profile updated successfully!';
}
