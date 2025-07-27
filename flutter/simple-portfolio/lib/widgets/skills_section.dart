import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:responsive_framework/responsive_framework.dart';

class Skill {
  final String name;
  final double proficiency;
  final String category;
  final IconData icon;

  const Skill({
    required this.name,
    required this.proficiency,
    required this.category,
    required this.icon,
  });
}

class SkillsSection extends StatelessWidget {
  final List<Skill> skills;

  const SkillsSection({
    super.key,
    required this.skills,
  });

  @override
  Widget build(BuildContext context) {
    final isMobile = ResponsiveBreakpoints.of(context).isMobile;
    final isTablet = ResponsiveBreakpoints.of(context).isTablet;

    return Container(
      padding: EdgeInsets.symmetric(
        horizontal: isMobile
            ? 20.0
            : isTablet
                ? 40.0
                : 80.0,
        vertical: 60.0,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            'Skills & Expertise',
            style: Theme.of(context).textTheme.displayMedium,
          ).animate().fadeIn(duration: 1.seconds).slideX(
                begin: -0.2,
                end: 0,
                duration: 1.seconds,
              ),
          const SizedBox(height: 40),
          _buildSkillsGrid(context),
        ],
      ),
    );
  }

  Widget _buildSkillsGrid(BuildContext context) {
    final categories = skills.map((s) => s.category).toSet().toList();
    final isMobile = ResponsiveBreakpoints.of(context).isMobile;
    final isTablet = ResponsiveBreakpoints.of(context).isTablet;

    return Column(
      children: categories.map((category) {
        final categorySkills =
            skills.where((s) => s.category == category).toList();
        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              category,
              style: Theme.of(context).textTheme.titleLarge,
            ).animate().fadeIn(duration: 1.seconds).slideX(
                  begin: -0.2,
                  end: 0,
                  duration: 1.seconds,
                ),
            const SizedBox(height: 20),
            GridView.builder(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: isMobile
                    ? 1
                    : isTablet
                        ? 2
                        : 3,
                crossAxisSpacing: 20,
                mainAxisSpacing: 20,
                childAspectRatio: 3,
              ),
              itemCount: categorySkills.length,
              itemBuilder: (context, index) {
                return _buildSkillCard(context, categorySkills[index], index);
              },
            ),
            const SizedBox(height: 40),
          ],
        );
      }).toList(),
    );
  }

  Widget _buildSkillCard(BuildContext context, Skill skill, int index) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(
                  skill.icon,
                  color: Theme.of(context).colorScheme.primary,
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(
                    skill.name,
                    style: Theme.of(context).textTheme.titleMedium,
                  ),
                ),
                Text(
                  '${(skill.proficiency * 100).toInt()}%',
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                        color: Theme.of(context).colorScheme.primary,
                        fontWeight: FontWeight.bold,
                      ),
                ),
              ],
            ),
            const SizedBox(height: 8),
            ClipRRect(
              borderRadius: BorderRadius.circular(4),
              child: LinearProgressIndicator(
                value: skill.proficiency,
                backgroundColor:
                    Theme.of(context).colorScheme.primary.withOpacity(0.1),
                valueColor: AlwaysStoppedAnimation<Color>(
                  Theme.of(context).colorScheme.primary,
                ),
                minHeight: 8,
              ),
            ),
          ],
        ),
      ),
    ).animate().fadeIn(duration: 1.seconds).slideY(
          begin: 0.2,
          end: 0,
          duration: 1.seconds,
          delay: Duration(milliseconds: 200 * index),
        );
  }
}
