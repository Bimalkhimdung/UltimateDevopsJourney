# Payment App

A Flutter mobile application with Stripe payment integration and Firebase authentication.

## Features

- User authentication (sign up, sign in, sign out)
- Secure payment processing with Stripe
- Multiple currency support
- Payment history tracking
- User profile management
- Modern and clean UI design

## Technical Stack

- Flutter SDK 3.19.0
- Dart 3.3.0
- Firebase (Authentication, Firestore)
- Stripe Payment Integration
- Riverpod for state management

## Getting Started

### Prerequisites

- Flutter SDK (3.19.0 or later)
- Dart SDK (3.3.0 or later)
- Firebase project
- Stripe account

### Configuration

1. Clone the repository:
```bash
git clone https://github.com/yourusername/payment_app.git
cd payment_app
```

2. Install dependencies:
```bash
flutter pub get
```

3. Configure Firebase:
   - Create a new Firebase project
   - Add Android and iOS apps to your Firebase project
   - Download and add the configuration files:
     - `google-services.json` for Android
     - `GoogleService-Info.plist` for iOS

4. Configure Stripe:
   - Create a Stripe account
   - Get your publishable key and secret key
   - Update the keys in `lib/core/config/app_config.dart`

5. Run the app:
```bash
flutter run
```

## Project Structure

```
lib/
├── core/
│   ├── config/
│   │   └── app_config.dart
│   ├── error/
│   │   └── app_error.dart
│   ├── theme/
│   │   └── app_theme.dart
│   └── utils/
├── features/
│   ├── auth/
│   │   ├── providers/
│   │   ├── screens/
│   │   └── services/
│   ├── payment/
│   │   ├── providers/
│   │   ├── screens/
│   │   └── services/
│   └── navigation/
│       └── screens/
└── shared/
    ├── models/
    └── widgets/
```

## Architecture

The app follows clean architecture principles with the following layers:

- **Presentation Layer**: UI components and state management
- **Domain Layer**: Business logic and use cases
- **Data Layer**: Data sources and repositories

## State Management

The app uses Riverpod for state management, providing:
- Dependency injection
- State management
- Code generation
- Testing utilities

## Security

- Secure authentication with Firebase
- PCI-compliant payment processing with Stripe
- Data encryption in transit and at rest
- Secure storage of sensitive information

## Testing

Run tests using:
```bash
flutter test
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flutter team for the amazing framework
- Firebase for authentication and database services
- Stripe for payment processing
- Riverpod for state management 