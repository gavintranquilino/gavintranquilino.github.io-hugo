---
title: "<strong>Remote-controlled</strong> LED"
date: "2021-02-07"
imageUrl: "/img/arduino-led.png"
subtitle: "RGB!!! YEAHHH!!!"
---

## Project Demonstration

{{< my_video_embed src="https://www.youtube.com/embed/48NtL1gEZPk" title="YouTube video player" >}}

## Source Code
```cpp
#include <IRremote.h>
#define MAX_TIME 150

IRrecv irrecv(6);
decode_results results;

long lastPressTime = 0;
long ON_BUTTON = 16753245;
long B_ONE = 16724175;

long red = 255;
long green = 255;
long blue = 255;

int redPin = 9;
int greenPin = 10;
int bluePin = 5;

bool state = false;

void RGB_colour(int red_val, int green_val, int blue_val) {
  // Function to output RGB values
  analogWrite(redPin, red_val);
  analogWrite(greenPin, green_val);
  analogWrite(bluePin, blue_val);
}

void setup() {
  Serial.begin(9600); // Start Serial Connection

  // Set pinMode for LED
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  irrecv.enableIRIn(); // Start the receiver
}

void loop() {
  if (irrecv.decode(&results)) { // Check to see if we received a code
    Serial.println(results.value);

    if (results.value == ON_BUTTON) {
      if (millis() - lastPressTime > MAX_TIME) {
        state = !state; // state = opposite of state
      }
      lastPressTime = millis();
    }

    if (results.value == B_ONE) {
      red = random(0, 256);
      green = random(0, 256);
      blue = random(0, 256);
      RGB_colour(red, green, blue);
    }

    irrecv.resume(); // Receive the next value
  }
}

```