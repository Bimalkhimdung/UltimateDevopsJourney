import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:payment_app/features/payment/services/payment_service.dart';

final paymentServiceProvider = Provider<PaymentService>((ref) {
  return PaymentService();
});

final paymentAmountProvider = StateProvider<double>((ref) => 0.0);

final selectedCurrencyProvider = StateProvider<String>((ref) => 'USD');

final isProcessingPaymentProvider = StateProvider<bool>((ref) => false);

final paymentErrorProvider = StateProvider<String?>((ref) => null);

final paymentControllerProvider =
    StateNotifierProvider<PaymentController, AsyncValue<void>>((ref) {
  return PaymentController(ref.watch(paymentServiceProvider));
});

class PaymentController extends StateNotifier<AsyncValue<void>> {
  final PaymentService _paymentService;

  PaymentController(this._paymentService) : super(const AsyncValue.data(null));

  Future<void> processPayment({
    required double amount,
    required String currency,
  }) async {
    state = const AsyncValue.loading();
    try {
      await _paymentService.processPayment(
        amount: amount,
        currency: currency,
      );
      state = const AsyncValue.data(null);
    } catch (e) {
      state = AsyncValue.error(e, StackTrace.current);
    }
  }

  Future<void> savePaymentMethod() async {
    state = const AsyncValue.loading();
    try {
      await _paymentService.savePaymentMethod();
      state = const AsyncValue.data(null);
    } catch (e) {
      state = AsyncValue.error(e, StackTrace.current);
    }
  }

  Future<void> deletePaymentMethod(String paymentMethodId) async {
    state = const AsyncValue.loading();
    try {
      await _paymentService.deletePaymentMethod(paymentMethodId);
      state = const AsyncValue.data(null);
    } catch (e) {
      state = AsyncValue.error(e, StackTrace.current);
    }
  }

  bool validatePaymentAmount(double amount) {
    return _paymentService.validatePaymentAmount(amount);
  }

  String formatCurrencyAmount(double amount, String currency) {
    return _paymentService.formatCurrencyAmount(amount, currency);
  }
}
