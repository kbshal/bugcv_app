import 'package:flutter/material.dart';
import 'DoctorHomePage.dart';

class DoctorScreen extends StatefulWidget {
  const DoctorScreen({Key? key}) : super(key: key);

  @override
  _DoctorScreenState createState() => _DoctorScreenState();
}

class _DoctorScreenState extends State<DoctorScreen> {
  bool Male = false;
  bool Female = false;
  final _formkey = GlobalKey<FormState>();

  final firstNameEditingController = TextEditingController();
  final secondNameEditingController = TextEditingController();
  final emailEditingController = TextEditingController();
  final passwordEditingController = TextEditingController();
  final phoneNumberEditingController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    //first name field
    final firstNameField = TextFormField(
      autofocus: false,
      controller: firstNameEditingController,
      keyboardType: TextInputType.name,
      //Validator: (){},
      onSaved: (value) {
        firstNameEditingController.text = 'value';
      },
      textInputAction: TextInputAction.next,
      decoration: const InputDecoration(
          prefixIcon: Icon(Icons.account_circle),
          contentPadding: EdgeInsets.fromLTRB(20, 15, 20, 15),
          prefixIconColor: Colors.red,
          border: OutlineInputBorder(),
          hintText: 'First Name '),
    );

    //second name field
    final secondNameField = TextFormField(
      autofocus: false,
      controller: secondNameEditingController,
      keyboardType: TextInputType.name,
      //Validator: (){},
      onSaved: (value) {
        secondNameEditingController.text = 'value';
      },
      textInputAction: TextInputAction.next,
      decoration: const InputDecoration(
          prefixIcon: Icon(Icons.account_circle),
          contentPadding: EdgeInsets.fromLTRB(20, 15, 20, 15),
          prefixIconColor: Colors.red,
          border: OutlineInputBorder(),
          hintText: 'Second Name '),
    );

    // email field
    final emailNameField = TextFormField(
      autofocus: false,
      controller: emailEditingController,
      keyboardType: TextInputType.emailAddress,
      //Validator: (){},
      onSaved: (value) {
        emailEditingController.text = 'value';
      },
      textInputAction: TextInputAction.next,
      decoration: const InputDecoration(
          prefixIcon: Icon(Icons.mail),
          contentPadding: EdgeInsets.fromLTRB(20, 15, 20, 15),
          prefixIconColor: Colors.red,
          border: OutlineInputBorder(),
          hintText: 'Email '),
    );

    //password field
    final passwordNameField = TextFormField(
      autofocus: false,
      controller: passwordEditingController,
      obscureText: true,
      //Validator: (){},
      onSaved: (value) {
        passwordEditingController.text = 'value';
      },
      textInputAction: TextInputAction.next,
      decoration: const InputDecoration(
          prefixIcon: Icon(Icons.vpn_key),
          contentPadding: EdgeInsets.fromLTRB(20, 15, 20, 15),
          prefixIconColor: Colors.red,
          border: OutlineInputBorder(),
          hintText: 'Password '),
    );

    //confirm password field
    final confirmpasswordField = TextFormField(
      autofocus: false,
      controller: phoneNumberEditingController,
      obscureText: true,
      //Validator: (){},
      onSaved: (value) {
        phoneNumberEditingController.text = 'value';
      },
      textInputAction: TextInputAction.done,
      decoration: const InputDecoration(
          prefixIcon: Icon(Icons.vpn_key),
          contentPadding: EdgeInsets.fromLTRB(20, 15, 20, 15),
          prefixIconColor: Colors.red,
          border: OutlineInputBorder(),
          hintText: 'Phone Number '),
    );
    //login button field

    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
          backgroundColor: Colors.transparent,
          elevation: 0,
          leading: IconButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              icon: const Icon(
                Icons.arrow_back,
                color: Colors.red,
              ))),
      body: Center(
          child: SingleChildScrollView(
        child: Container(
          color: Colors.white,
          child: Padding(
            padding: const EdgeInsets.all(36.0),
            child: Form(
              key: _formkey,
              child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: <Widget>[
                    SizedBox(
                        height: 200,
                        child: Image.asset(
                          "asset/images/Littman.jpg",
                          fit: BoxFit.contain,
                        )),
                    const SizedBox(height: 45),
                    firstNameField,
                    const SizedBox(height: 20),
                    secondNameField,
                    const SizedBox(height: 20),
                    emailNameField,
                    const SizedBox(height: 20),
                    passwordNameField,
                    const SizedBox(height: 20),
                    confirmpasswordField,
                    const SizedBox(
                      height: 20,
                    ),
                    const SizedBox(height: 45),
                    Container(
                      height: 50,
                      width: 250,
                      decoration: BoxDecoration(
                          color: Colors.redAccent,
                          borderRadius: BorderRadius.circular(20)),
                      child: TextButton(
                        onPressed: () {
                          Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (_) => const DoctorHomePage()));
                        },
                        child: const Text(
                          'Login',
                          style: TextStyle(color: Colors.black, fontSize: 25),
                        ),
                      ),
                    )
                  ]),
            ),
          ),
        ),
      )),
    );
  }
}
