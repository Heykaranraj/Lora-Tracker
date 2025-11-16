/*
   parent_keyboard_control.ino
   Use Serial Monitor keyboard keys to control the buzzer.
   Press 'b' -> buzzer ON
   Press 's' -> buzzer OFF
*/

#define LED_PIN      6
#define BUZZER_PIN   5

void setup() {
  Serial.begin(115200);

  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  analogWrite(LED_PIN, 0);
  digitalWrite(BUZZER_PIN, LOW);

  //Serial.println("Keyboard control active:");
  //Serial.println("Press 'b' + ENTER  -> BUZZER ON");
  //Serial.println("Press 's' + ENTER  -> BUZZER OFF");
}

void loop() {

  if (Serial.available()) {
    char key = Serial.read();

    if (key == 'b') {
      Serial.println("BUZZER ON");
      tone(BUZZER_PIN, 1000);   // 1 kHz alarm
      analogWrite(LED_PIN, 255);
    }

    if (key == 's') {
      Serial.println("BUZZER OFF");
      noTone(BUZZER_PIN);
      analogWrite(LED_PIN, 0);
    }
  }
}
