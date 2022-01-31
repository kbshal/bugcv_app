import 'package:flutter/material.dart';

class Menu extends StatelessWidget {
  const Menu({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.purple,
        body: Column(
          children: <Widget>[
            Container(
              height: 265,
              child: Image.asset('asset/images/Doctor.png'),
            ),
            Container(
              padding: const EdgeInsets.fromLTRB(30, 20, 45, 5),
              alignment: Alignment.centerLeft,
              child: const Text(
                'Welcome',
                style: TextStyle(
                    fontSize: 28,
                    fontWeight: FontWeight.bold,
                    color: Colors.yellow),
              ),
            ),
            Container(
              padding: const EdgeInsets.all(30),
              child: const Text(
                'Get your Doctor without even going to the hospital',
                style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.w500,
                    color: Colors.white),
              ),
            ),
            Container(
              padding: const EdgeInsets.fromLTRB(15, 10, 230, 30),
              child: const Text('Are You a',
                  style: TextStyle(
                      fontSize: 25,
                      fontWeight: FontWeight.normal,
                      color: Colors.yellow)),
            ),
            Row(
              children: <Widget>[
                Container(
                  padding: const EdgeInsets.fromLTRB(50, 10, 10, 10),
                  child: const Text(
                    'Patient',
                    style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.normal,
                        color: Colors.white),
                  ),
                ),
              ],
            )
          ],
        ));
  }
}
