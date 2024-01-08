void main(List<String> args) {
  var  list = [1,2,3,4,5];
   for (var i in list) {
     for (var j = 0; j < 5; j++) {
       print(i);
     }

   }

   //let's create our class instance
    var person = Person('John', 30);

    person.showOutput();
   
}


// Let's create a class

class Person {
  String name;
  int age;
  Person(this.name, this.age);
  void showOutput() {
    print(name);
    print(age);
  }
}