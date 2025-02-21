int sp=5;
int l=8;
int r=7;

void setup() {
Serial.begin(9600);
pinMode(sp,OUTPUT);
pinMode(l,OUTPUT);
pinMode(r,OUTPUT);
}

void stop(){
  Serial.println("Motor durduruldu");
  digitalWrite(l,LOW);
  digitalWrite(r,LOW);
  analogWrite(sp,100);
  delay(2000);
}

void loop() {
  Serial.println("Motor yarım güçte sola döndürülüyor");
  digitalWrite(l,HIGH);
  digitalWrite(r,LOW);
  analogWrite(sp,150);
  delay(3000);

  stop();

  Serial.println("Motor yarım güçte sağa döndürülüyor");
  digitalWrite(l,LOW);
  digitalWrite(r,HIGH);
  analogWrite(sp,150);
  delay(3000);
  
  stop();

  Serial.println("Motor TAM güçte sola döndürülüyor");
  digitalWrite(l,HIGH);
  digitalWrite(r,LOW);
  analogWrite(sp,255);
  delay(3000);

  stop();

  Serial.println("Motor TAM güçte sağa döndürülüyor");
  digitalWrite(l,LOW);
  digitalWrite(r,HIGH);
  analogWrite(sp,255);
  delay(3000);

  stop();
  

}
