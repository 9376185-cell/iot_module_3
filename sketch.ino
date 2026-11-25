const int TRIG_PIN = 9;
const int ECHO_PIN = 10;

const float TANK_HEIGHT_CM = 100.0;

unsigned long sampleIndex = 0;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  Serial.println("time_s,distance_cm,water_level_cm");
}

float measureDistanceCm() {
  
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  if (duration == 0) {
    return TANK_HEIGHT_CM;
  }

  float distance = (duration * 0.0343) / 2.0;
  return constrain(distance, 0.0, TANK_HEIGHT_CM);
}

void loop() {
  float distanceCm = measureDistanceCm();
  float waterLevelCm = TANK_HEIGHT_CM - distanceCm;

  Serial.print(sampleIndex);
  Serial.print(",");
  Serial.print(distanceCm, 2);
  Serial.print(",");
  Serial.println(waterLevelCm, 2);

  sampleIndex++;
  delay(1000); 
}