import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';

class NavBar extends StatelessWidget {
  const NavBar({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 80,
      color: Colors.transparent,
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 40),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(
              'Portfolio',
              style: Theme.of(context).textTheme.titleLarge?.copyWith(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                  ),
            ).animate().fadeIn(duration: 1.seconds),
            Row(
              children: [
                _buildNavItem(context, 'Home', 0),
                _buildNavItem(context, 'Projects', 1),
                _buildNavItem(context, 'Skills', 2),
                _buildNavItem(context, 'Contact', 3),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildNavItem(BuildContext context, String label, int index) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20),
      child: TextButton(
        onPressed: () {
          // TODO: Implement smooth scroll to section
        },
        child: Text(
          label,
          style: const TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.w500,
          ),
        ),
      ),
    ).animate().fadeIn(
          duration: 1.seconds,
          delay: Duration(milliseconds: 200 * index),
        );
  }
}
