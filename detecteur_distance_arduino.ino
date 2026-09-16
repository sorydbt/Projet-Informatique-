int bouton = 7;
int led = 8;

void setup() {
  pinMode(bouton, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  int valeur = digitalRead(bouton);

  if (valeur == HIGH) {
    digitalWrite(led, HIGH);
  } else {
    digitalWrite(led, LOW);
  }
}
