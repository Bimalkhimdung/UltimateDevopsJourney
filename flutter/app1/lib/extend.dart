class Animal {
  String name;

  Animal(this.name);

  void makeSound() {
    print("Generic animal sound");
  }
}


class Cat extends Animal {
  String color;

  Cat(super.name, this.color); // Calling the Animal constructor

  @override
  void makeSound() {
    print("Meow!"); // Overriding the makeSound method
  }

  void purr() {
    print("Purrrr...");
  }
}

void main() {
  var cat = Cat("Whiskers", "White");
  cat.makeSound(); // Output: Meow!
  cat.purr(); // Output: Purrrr...
}
