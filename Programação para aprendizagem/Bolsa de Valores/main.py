/**
 * @file main.cpp
 * @author DaveK2 (davefr@outlook.com.br)
 * @brief Codigo de controle de acesso da porta do NSC (Nilton Do Sexo)
 * utilizando esp32IFF Bom Jesus do Itabapoana
 * @version 0.1
 * @date 2023-02-03
 *
 * @copyright Copyright (c) 2023
 *
 */

// SS/SDA GPIO5
// SCK GPIO18
// MOSI GPIO23
// MISO GPIO19
// RST GPIO27

#include <Arduino.h>
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 5   // ESP32 pin GIOP5
#define RST_PIN 27 // ESP32 pin GIOP27
#define OUTPIN 2

String conteudo; // cria uma string
String idPermitido[] = {"53 2B 12 EB 20 00 01",
                        "53 2C 05 EB 20 00 01", "53 35 0C EB 20 00 01", "53 9F 0F EB 20 00 01"};

MFRC522 mfrc522(SS_PIN, RST_PIN);

void readCard();
void unlockDoor();

void setup()
{
  Serial.begin(115200);
  SPI.begin();        // init SPI bus
  mfrc522.PCD_Init(); // init MFRC522

  pinMode(OUTPIN, OUTPUT);

  Serial.println("Tap an RFID/NFC tag on the RFID-RC522 reader");
}

void loop()
{
  readCard();
}

/**
 * @brief le cartao rfid
 *
 */
void readCard()
{
  conteudo = "";
  if (!mfrc522.PICC_IsNewCardPresent())
  {
    return; // se nao tiver um cartao para ser lido recomeça o void loop
  }
  if (!mfrc522.PICC_ReadCardSerial())
  {
    return; // se nao conseguir ler o cartao recomeça o void loop tambem
  }
  Serial.print("id da tag :"); // imprime na serial o id do cartao

  for (byte i = 0; i < mfrc522.uid.size; i++)
  { // faz uma verificacao dos bits da memoria do cartao
    // ambos comandos abaixo vão concatenar as informacoes do cartao...
    // porem os 2 primeiros irao mostrar na serial e os 2 ultimos guardarao os valores na string de conteudo para fazer as verificacoes
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
    conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
    conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  conteudo.toUpperCase();
  Serial.println();
  unlockDoor();
  // instrui o PICC quando no estado ACTIVE a ir para um estado de "parada"
  mfrc522.PICC_HaltA();
  // "stop" a encriptação do PCD, deve ser chamado após a comunicação com autenticação, caso contrário novas comunicações não poderão ser iniciadas
  mfrc522.PCD_StopCrypto1();
}

/**
 * @brief destranca a porta
 *
 */
void unlockDoor()
{
  for (int i = 0; i < sizeof(idPermitido) / sizeof(String); i++)
  {
    if (conteudo.substring(1) == idPermitido[i])
    {
      Serial.println("Acesso concedido");
      digitalWrite(OUTPIN, HIGH);
      break;
    }
  }
  Serial.println(digitalRead(OUTPIN));
  digitalWrite(OUTPIN, LOW);
}
