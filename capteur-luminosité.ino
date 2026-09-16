int lumiere = A0;
int pompe = 8;
int buzzer = 9;

void setup() {
  pinMode(pompe, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  int valeur = analogRead(lumiere);

  if (valeur > 700) {
    digitalWrite(pompe, HIGH);
    tone(buzzer, 1000);
    delay(3000);
    digitalWrite(pompe, LOW);
    noTone(buzzer);
  }
}
