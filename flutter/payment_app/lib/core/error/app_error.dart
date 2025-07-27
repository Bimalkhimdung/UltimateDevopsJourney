class AppError implements Exception {
  final String message;
  final String? code;
  final dynamic originalError;

  AppError({
    required this.message,
    this.code,
    this.originalError,
  });

  @override
  String toString() =>
      'AppError: $message${code != null ? ' (Code: $code)' : ''}';

  factory AppError.network() {
    return AppError(
      message: 'Network error occurred. Please check your connection.',
      code: 'NETWORK_ERROR',
    );
  }

  factory AppError.payment() {
    return AppError(
      message: 'Payment processing failed. Please try again.',
      code: 'PAYMENT_ERROR',
    );
  }

  factory AppError.authentication() {
    return AppError(
      message: 'Authentication failed. Please login again.',
      code: 'AUTH_ERROR',
    );
  }

  factory AppError.validation(String message) {
    return AppError(
      message: message,
      code: 'VALIDATION_ERROR',
    );
  }

  factory AppError.unknown(dynamic error) {
    return AppError(
      message: 'An unexpected error occurred.',
      code: 'UNKNOWN_ERROR',
      originalError: error,
    );
  }
}
