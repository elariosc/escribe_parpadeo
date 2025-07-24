/* Esta version del codigo utiliza un sensor Infra rojo
Cuando el sensor no detecta, manda cero (LOW)
y cuando detecta, manda 1 (HIGH)
*/
const int buttonPin = PD2;   // Pin del botón
const int buzzerPin = PD4;   // Pin del buzzer
const int debounceTime = 400;  // Tiempo de debounce para prendido en milisegundos (ajustable)
const int debounceTimeOff = 100;  // Tiempo de debounce para apagado en milisegundos (ajustable)

bool buttonPressed = false;  // Estado del botón

void setup() {
  // put your setup code here, to run once:
  pinMode(buttonPin, INPUT_PULLUP); // Botón con resistencia interna
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);  // Iniciar comunicación serie
}

void loop() {
  // put your main code here, to run repeatedly:
      if (digitalRead(buttonPin) == HIGH && !buttonPressed) {  
        delay(debounceTime);  // Espera para debounce
        if (digitalRead(buttonPin) == HIGH) {  // Verificar si sigue presionado
            buttonPressed = true;
            digitalWrite(buzzerPin, HIGH);  // Activar buzzer
            Serial.println("ENTER");  // Enviar señal a la PC
        }
    }

    if (digitalRead(buttonPin) == LOW && buttonPressed) {  
        delay(debounceTimeOff);  // Espera para debounce en liberación
        if (digitalRead(buttonPin) == LOW) {  // Verificar si sigue liberado
            buttonPressed = false;
            digitalWrite(buzzerPin, LOW);  // Apagar buzzer
            Serial.println("RELEASE");  // Enviar señal de liberación
        }
    }
}
