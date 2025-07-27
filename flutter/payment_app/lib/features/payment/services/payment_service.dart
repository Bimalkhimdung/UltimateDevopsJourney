import 'package:flutter_stripe/flutter_stripe.dart';
import 'package:payment_app/core/config/app_config.dart';
import 'package:payment_app/core/error/app_error.dart';

class PaymentService {
  // Create a payment intent
  Future<PaymentIntent> createPaymentIntent({
    required double amount,
    required String currency,
  }) async {
    try {
      // In a real app, you would make an API call to your backend
      // to create a payment intent. For this example, we'll create it directly.
      final paymentIntent = await Stripe.instance.createPaymentIntent(
        params: PaymentIntentParams(
          amount: (amount * 100).toInt(), // Convert to cents
          currency: currency,
          paymentMethodTypes: ['card'],
        ),
      );
      return paymentIntent;
    } catch (e) {
      throw AppError.payment();
    }
  }

  // Process payment
  Future<void> processPayment({
    required double amount,
    required String currency,
  }) async {
    try {
      // Create payment intent
      final paymentIntent = await createPaymentIntent(
        amount: amount,
        currency: currency,
      );

      // Confirm payment
      await Stripe.instance.confirmPayment(
        paymentIntent.clientSecret,
        const PaymentMethodParams.card(paymentMethodData: PaymentMethodData()),
      );
    } catch (e) {
      throw AppError.payment();
    }
  }

  // Save payment method
  Future<void> savePaymentMethod() async {
    try {
      // Create payment method
      final paymentMethod = await Stripe.instance.createPaymentMethod(
        params: const PaymentMethodParams.card(
          paymentMethodData: PaymentMethodData(),
        ),
      );

      // In a real app, you would save the payment method ID to your backend
      // and associate it with the user's account
      print('Payment method saved: ${paymentMethod.id}');
    } catch (e) {
      throw AppError.payment();
    }
  }

  // Get saved payment methods
  Future<List<PaymentMethod>> getSavedPaymentMethods() async {
    try {
      // In a real app, you would fetch the saved payment methods from your backend
      // For this example, we'll return an empty list
      return [];
    } catch (e) {
      throw AppError.payment();
    }
  }

  // Delete payment method
  Future<void> deletePaymentMethod(String paymentMethodId) async {
    try {
      // In a real app, you would delete the payment method from your backend
      // For this example, we'll just print the ID
      print('Payment method deleted: $paymentMethodId');
    } catch (e) {
      throw AppError.payment();
    }
  }

  // Validate payment amount
  bool validatePaymentAmount(double amount) {
    return amount >= AppConfig.minimumPaymentAmount &&
        amount <= AppConfig.maximumPaymentAmount;
  }

  // Format currency amount
  String formatCurrencyAmount(double amount, String currency) {
    return '${currency.toUpperCase()} ${amount.toStringAsFixed(2)}';
  }
}
