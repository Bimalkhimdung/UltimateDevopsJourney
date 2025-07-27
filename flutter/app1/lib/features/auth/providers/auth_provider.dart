import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:payment_app/features/auth/services/auth_service.dart';
import 'package:payment_app/shared/models/user_model.dart';

final authServiceProvider = Provider<AuthService>((ref) {
  return AuthService();
});

final authStateProvider = StreamProvider<User?>((ref) {
  return ref.watch(authServiceProvider).authStateChanges;
});

final userProvider = FutureProvider<UserModel?>((ref) async {
  final authService = ref.watch(authServiceProvider);
  final user = authService.currentUser;
  if (user == null) return null;

  try {
    return await authService._getUserData(user.uid);
  } catch (e) {
    return null;
  }
});

final authControllerProvider =
    StateNotifierProvider<AuthController, AsyncValue<UserModel?>>((ref) {
  return AuthController(ref.watch(authServiceProvider));
});

class AuthController extends StateNotifier<AsyncValue<UserModel?>> {
  final AuthService _authService;

  AuthController(this._authService) : super(const AsyncValue.loading()) {
    _init();
  }

  Future<void> _init() async {
    final user = _authService.currentUser;
    if (user == null) {
      state = const AsyncValue.data(null);
      return;
    }

    try {
      final userData = await _authService._getUserData(user.uid);
      state = AsyncValue.data(userData);
    } catch (e) {
      state = AsyncValue.error(e, StackTrace.current);
    }
  }

  Future<void> signIn(String email, String password) async {
    state = const AsyncValue.loading();
    try {
      final user =
          await _authService.signInWithEmailAndPassword(email, password);
      state = AsyncValue.data(user);
    } catch (e) {
      state = AsyncValue.error(e, StackTrace.current);
    }
  }

  Future<void> register(
      String email, String password, String displayName) async {
    state = const AsyncValue.loading();
    try {
      final user = await _authService.registerWithEmailAndPassword(
        email,
        password,
        displayName,
      );
      state = AsyncValue.data(user);
    } catch (e) {
      state = AsyncValue.error(e, StackTrace.current);
    }
  }

  Future<void> signOut() async {
    try {
      await _authService.signOut();
      state = const AsyncValue.data(null);
    } catch (e) {
      state = AsyncValue.error(e, StackTrace.current);
    }
  }

  Future<void> updateProfile({String? displayName, String? photoUrl}) async {
    try {
      final user = await _authService.updateProfile(
        displayName: displayName,
        photoUrl: photoUrl,
      );
      state = AsyncValue.data(user);
    } catch (e) {
      state = AsyncValue.error(e, StackTrace.current);
    }
  }
}
