input.onButtonPressed(Button.A, function () {
    radiogroup += 5
    if (radiogroup >= 11) {
        radiogroup = 1
    }
    radio.setGroup(radiogroup)
    basic.showString("" + radiogroup)
})
input.onButtonPressed(Button.AB, function () {
    radiogroup += 1
    if (radiogroup == 11) {
        radiogroup = 1
    }
    radio.setGroup(radiogroup)
    basic.showString("" + radiogroup)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    radiogroup += -5
    if (radiogroup <= 0) {
        radiogroup = 1
    }
    radio.setGroup(radiogroup)
    basic.showString("" + radiogroup)
})
radio.onReceivedValue(function (name, value) {
    if (name == "x") {
        x = value
    }
    if (name == "y") {
        y = value
    }
})
let y = 0
let x = 0
let radiogroup = 0
radiogroup = 1
radio.setGroup(radiogroup)
basic.showString("" + radiogroup)
basic.forever(function () {
    if (-40 < x && x < 40) {
        x = 0
    }
    if (-40 < y && y < 40) {
        y = 0
    }
    if (y > 0) {
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.digitalWritePin(DigitalPin.P8, 1)
        pins.digitalWritePin(DigitalPin.P16, 1)
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
    if (y < 0) {
        pins.digitalWritePin(DigitalPin.P12, 1)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P16, 0)
        pins.digitalWritePin(DigitalPin.P0, 1)
    }
    if (x > 0) {
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P16, 1)
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
    if (x < 0) {
        pins.digitalWritePin(DigitalPin.P12, 1)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P16, 0)
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
    if (x == 0 && y == 0) {
        pins.digitalWritePin(DigitalPin.P12, 0)
        pins.digitalWritePin(DigitalPin.P8, 0)
        pins.digitalWritePin(DigitalPin.P16, 0)
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
    basic.pause(50)
})
