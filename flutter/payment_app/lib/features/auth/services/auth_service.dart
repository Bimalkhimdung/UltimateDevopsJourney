import 'package:firebase_auth/firebase_auth.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:payment_app/core/error/app_error.dart';
import 'package:payment_app/shared/models/user_model.dart';

class AuthService {
  final FirebaseAuth _auth = FirebaseAuth.instance;
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  // Get current user
  User? get currentUser => _auth.currentUser;

  // Stream of auth state changes
  Stream<User?> get authStateChanges => _auth.authStateChanges();

  // Sign in with email and password
  Future<UserModel> signInWithEmailAndPassword(
      String email, String password) async {
    try {
      final UserCredential result = await _auth.signInWithEmailAndPassword(
        email: email,
        password: password,
      );

      final User? user = result.user;
      if (user == null) {
        throw AppError.authentication();
      }

      // Update last login time
      await _firestore.collection('users').doc(user.uid).update({
        'lastLoginAt': FieldValue.serverTimestamp(),
      });

      return await _getUserData(user.uid);
    } on FirebaseAuthException catch (e) {
      throw AppError(
        message: e.message ?? 'Authentication failed',
        code: e.code,
      );
    } catch (e) {
      throw AppError.unknown(e);
    }
  }

  // Register with email and password
  Future<UserModel> registerWithEmailAndPassword(
    String email,
    String password,
    String displayName,
  ) async {
    try {
      final UserCredential result = await _auth.createUserWithEmailAndPassword(
        email: email,
        password: password,
      );

      final User? user = result.user;
      if (user == null) {
        throw AppError.authentication();
      }

      // Update user profile
      await user.updateDisplayName(displayName);

      // Create user document in Firestore
      final userModel = UserModel(
        id: user.uid,
        email: email,
        displayName: displayName,
        createdAt: DateTime.now(),
        lastLoginAt: DateTime.now(),
      );

      await _firestore
          .collection('users')
          .doc(user.uid)
          .set(userModel.toJson());

      return userModel;
    } on FirebaseAuthException catch (e) {
      throw AppError(
        message: e.message ?? 'Registration failed',
        code: e.code,
      );
    } catch (e) {
      throw AppError.unknown(e);
    }
  }

  // Sign out
  Future<void> signOut() async {
    try {
      await _auth.signOut();
    } catch (e) {
      throw AppError.unknown(e);
    }
  }

  // Get user data from Firestore
  Future<UserModel> _getUserData(String uid) async {
    try {
      final doc = await _firestore.collection('users').doc(uid).get();
      if (!doc.exists) {
        throw AppError(
          message: 'User data not found',
          code: 'USER_NOT_FOUND',
        );
      }
      return UserModel.fromJson(doc.data()!);
    } catch (e) {
      throw AppError.unknown(e);
    }
  }

  // Update user profile
  Future<UserModel> updateProfile({
    String? displayName,
    String? photoUrl,
  }) async {
    try {
      final user = currentUser;
      if (user == null) {
        throw AppError.authentication();
      }

      final updates = <String, dynamic>{};
      if (displayName != null) {
        await user.updateDisplayName(displayName);
        updates['displayName'] = displayName;
      }
      if (photoUrl != null) {
        await user.updatePhotoURL(photoUrl);
        updates['photoUrl'] = photoUrl;
      }

      if (updates.isNotEmpty) {
        await _firestore.collection('users').doc(user.uid).update(updates);
      }

      return await _getUserData(user.uid);
    } catch (e) {
      throw AppError.unknown(e);
    }
  }
}
