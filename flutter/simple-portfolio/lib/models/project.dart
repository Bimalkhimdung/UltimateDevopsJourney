class Project {
  final String id;
  final String title;
  final String description;
  final String imageUrl;
  final List<String> technologies;
  final String? projectUrl;
  final String? githubUrl;
  final List<String> features;
  final DateTime date;

  Project({
    required this.id,
    required this.title,
    required this.description,
    required this.imageUrl,
    required this.technologies,
    this.projectUrl,
    this.githubUrl,
    required this.features,
    required this.date,
  });

  factory Project.fromJson(Map<String, dynamic> json) {
    return Project(
      id: json['id'] as String,
      title: json['title'] as String,
      description: json['description'] as String,
      imageUrl: json['imageUrl'] as String,
      technologies: List<String>.from(json['technologies'] as List),
      projectUrl: json['projectUrl'] as String?,
      githubUrl: json['githubUrl'] as String?,
      features: List<String>.from(json['features'] as List),
      date: DateTime.parse(json['date'] as String),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'description': description,
      'imageUrl': imageUrl,
      'technologies': technologies,
      'projectUrl': projectUrl,
      'githubUrl': githubUrl,
      'features': features,
      'date': date.toIso8601String(),
    };
  }
}
