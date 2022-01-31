import 'package:finance_app/screens/DoctorScreen.dart';
import 'package:flutter/material.dart';
import 'package:finance_app/Homepage.dart';
import 'package:finance_app/SignUp.dart';

import 'ForgotPassword.dart';

class LoginDemo extends StatefulWidget {
  @override
  _LoginDemoState createState() => _LoginDemoState();
}

class _LoginDemoState extends State<LoginDemo> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Column(children: <Widget>[
          Padding(
              padding: const EdgeInsets.only(top: 60.0),
              child: Center(
                  child: Container(
                width: 200,
                height: 150,
                child: Image.asset('asset/images/Logo2.png'),
              ))),
          const SizedBox(height: 45),
          const Padding(
            padding: EdgeInsets.symmetric(horizontal: 15),
            child: TextField(
              decoration: InputDecoration(
                  prefixIcon: Icon(Icons.mail),
                  prefixIconColor: Colors.red,
                  border: OutlineInputBorder(),
                  labelText: 'Username',
                  hintText: 'Enter valid email id '),
              textInputAction: TextInputAction.next,
            ),
          ),
          const Padding(
            padding:
                EdgeInsets.only(left: 15.0, right: 15.0, top: 15, bottom: 0),
            child: TextField(
                obscureText: true,
                decoration: InputDecoration(
                    prefixIcon: Icon(Icons.vpn_key),
                    border: OutlineInputBorder(),
                    labelText: 'Password',
                    hintText: 'Enter secure password'),
                textInputAction: TextInputAction.done),
          ),
          const SizedBox(
            height: 30,
          ),
          const Align(alignment: Alignment.bottomCenter),
          FlatButton(
            onPressed: () {
              Navigator.push(context,
                  MaterialPageRoute(builder: (_) => const ForgotPassword()));
            },
            child: const Text(
              'Forgot Password',
              style: TextStyle(color: Colors.red, fontSize: 15),
            ),
          ),
          const SizedBox(height: 45),
          Container(
            height: 50,
            width: 250,
            decoration: BoxDecoration(
                color: Colors.purple, borderRadius: BorderRadius.circular(20)),
            child: TextButton(
              onPressed: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (_) => const Homepage()));
              },
              child: const Text(
                'Login',
                style: TextStyle(color: Colors.blue, fontSize: 25),
              ),
            ),
          ),
          const SizedBox(height: 30),
          Container(
              height: 50,
              width: 250,
              decoration: BoxDecoration(
                  color: Colors.white, borderRadius: BorderRadius.circular(20)),
              child: TextButton(
                  child: const Text('Create Account',
                      style: TextStyle(color: Colors.black)),
                  onPressed: () {
                    Navigator.push(context,
                        MaterialPageRoute(builder: (_) => const SignUp()));
                  })),
          SizedBox(
            height: 30,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Text('Are you a Doctor?'),
              GestureDetector(
                onTap: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (_) => const DoctorScreen()));
                },
                child: const Text(
                  'Click Here',
                  style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.redAccent),
                ),
              )
            ],
          )
        ]),
      ),
    );
  }
}
