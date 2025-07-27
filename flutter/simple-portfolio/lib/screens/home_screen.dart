import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:responsive_framework/responsive_framework.dart';
import '../models/project.dart';
import '../widgets/projects_section.dart';
import '../widgets/skills_section.dart';
import '../widgets/contact_section.dart';
import '../widgets/nav_bar.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Column(
          children: [
            const NavBar(),
            _buildHeroSection(context),
            ProjectsSection(
              projects: _getSampleProjects(),
            ),
            SkillsSection(
              skills: _getSampleSkills(),
            ),
            const ContactSection(),
          ],
        ),
      ),
    );
  }

  List<Skill> _getSampleSkills() {
    return [
      // Programming Languages
      const Skill(
        name: 'Dart',
        proficiency: 0.9,
        category: 'Programming Languages',
        icon: Icons.code,
      ),
      const Skill(
        name: 'JavaScript',
        proficiency: 0.85,
        category: 'Programming Languages',
        icon: Icons.code,
      ),
      const Skill(
        name: 'Python',
        proficiency: 0.8,
        category: 'Programming Languages',
        icon: Icons.code,
      ),
      // Frameworks
      const Skill(
        name: 'Flutter',
        proficiency: 0.95,
        category: 'Frameworks',
        icon: Icons.phone_android,
      ),
      const Skill(
        name: 'React',
        proficiency: 0.85,
        category: 'Frameworks',
        icon: Icons.web,
      ),
      const Skill(
        name: 'Node.js',
        proficiency: 0.8,
        category: 'Frameworks',
        icon: Icons.storage,
      ),
      // Tools & Technologies
      const Skill(
        name: 'Git',
        proficiency: 0.9,
        category: 'Tools & Technologies',
        icon: Icons.terminal,
      ),
      const Skill(
        name: 'Docker',
        proficiency: 0.75,
        category: 'Tools & Technologies',
        icon: Icons.dns,
      ),
      const Skill(
        name: 'AWS',
        proficiency: 0.7,
        category: 'Tools & Technologies',
        icon: Icons.cloud,
      ),
    ];
  }

  List<Project> _getSampleProjects() {
    return [
      Project(
        id: '1',
        title: 'E-Commerce App',
        description:
            'A modern e-commerce application built with Flutter and Firebase.',
        imageUrl: 'https://picsum.photos/800/600',
        technologies: ['Flutter', 'Firebase', 'Provider', 'Stripe'],
        projectUrl: 'https://example.com',
        githubUrl: 'https://github.com',
        features: [
          'User Authentication',
          'Product Catalog',
          'Shopping Cart',
          'Payment Integration',
        ],
        date: DateTime.now(),
      ),
      Project(
        id: '2',
        title: 'Social Media Dashboard',
        description:
            'A comprehensive dashboard for managing social media accounts.',
        imageUrl: 'https://picsum.photos/800/601',
        technologies: ['Flutter', 'GraphQL', 'AWS', 'Dart'],
        projectUrl: 'https://example.com',
        githubUrl: 'https://github.com',
        features: [
          'Analytics Dashboard',
          'Content Scheduling',
          'Engagement Tracking',
          'Multi-platform Support',
        ],
        date: DateTime.now(),
      ),
      Project(
        id: '3',
        title: 'Fitness Tracker',
        description: 'A mobile app for tracking workouts and nutrition.',
        imageUrl: 'https://picsum.photos/800/602',
        technologies: ['Flutter', 'SQLite', 'BLoC', 'Charts'],
        projectUrl: 'https://example.com',
        githubUrl: 'https://github.com',
        features: [
          'Workout Tracking',
          'Nutrition Log',
          'Progress Charts',
          'Goal Setting',
        ],
        date: DateTime.now(),
      ),
    ];
  }

  Widget _buildHeroSection(BuildContext context) {
    final isMobile = ResponsiveBreakpoints.of(context).isMobile;
    final isTablet = ResponsiveBreakpoints.of(context).isTablet;

    return Container(
      height: MediaQuery.of(context).size.height,
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [
            Theme.of(context).colorScheme.primary,
            Theme.of(context).colorScheme.secondary,
          ],
        ),
      ),
      child: Stack(
        children: [
          // Background animated circles
          ...List.generate(
            3,
            (index) => Positioned(
              top: 100.0 * (index + 1),
              left: 50.0 * (index + 1),
              child: Container(
                width: 200.0 * (index + 1),
                height: 200.0 * (index + 1),
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: Colors.white.withOpacity(0.1),
                ),
              ).animate().fadeIn(duration: 1.seconds).scale(
                    begin: const Offset(0.8, 0.8),
                    end: const Offset(1.0, 1.0),
                    duration: 2.seconds,
                  ),
            ),
          ),
          // Content
          Center(
            child: Padding(
              padding: EdgeInsets.symmetric(
                horizontal: isMobile
                    ? 20.0
                    : isTablet
                        ? 40.0
                        : 80.0,
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Hi, I\'m [Your Name]',
                    style: Theme.of(context).textTheme.displayLarge?.copyWith(
                          color: Colors.white,
                          fontSize: isMobile
                              ? 32
                              : isTablet
                                  ? 48
                                  : 64,
                        ),
                  ).animate().fadeIn(duration: 1.seconds).slideX(
                        begin: -0.2,
                        end: 0,
                        duration: 1.seconds,
                      ),
                  const SizedBox(height: 20),
                  Text(
                    'Flutter Developer & UI/UX Designer',
                    style: Theme.of(context).textTheme.displaySmall?.copyWith(
                          color: Colors.white.withOpacity(0.9),
                          fontSize: isMobile
                              ? 20
                              : isTablet
                                  ? 24
                                  : 32,
                        ),
                  ).animate().fadeIn(duration: 1.seconds).slideX(
                        begin: -0.2,
                        end: 0,
                        duration: 1.seconds,
                        delay: 200.milliseconds,
                      ),
                  const SizedBox(height: 40),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.start,
                    children: [
                      _buildActionButton(
                        context,
                        'View Projects',
                        Icons.work,
                        () {
                          // Navigate to projects
                        },
                      ),
                      const SizedBox(width: 20),
                      _buildActionButton(
                        context,
                        'Contact Me',
                        Icons.mail,
                        () {
                          // Navigate to contact
                        },
                      ),
                    ],
                  ).animate().fadeIn(duration: 1.seconds).slideY(
                        begin: 0.2,
                        end: 0,
                        duration: 1.seconds,
                        delay: 400.milliseconds,
                      ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildActionButton(
    BuildContext context,
    String text,
    IconData icon,
    VoidCallback onPressed,
  ) {
    return ElevatedButton.icon(
      onPressed: onPressed,
      icon: Icon(icon),
      label: Text(text),
      style: ElevatedButton.styleFrom(
        backgroundColor: Colors.white,
        foregroundColor: Theme.of(context).colorScheme.primary,
        padding: const EdgeInsets.symmetric(
          horizontal: 24,
          vertical: 16,
        ),
      ),
    );
  }
}
