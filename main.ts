input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showString("S")
    serial.writeLine("kusuguttaikarayamete-")
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    basic.showString("A")
    serial.writeLine("gya")
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("Y")
    serial.writeLine("sorawotobuzo-")
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Silly)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("B")
    serial.writeLine("o-no-")
    basic.clearScreen()
})
for (let index = 0; index < 4; index++) {
    basic.showIcon(IconNames.Square)
}
serial.redirect(
SerialPin.P1,
SerialPin.P0,
BaudRate.BaudRate9600
)
basic.forever(function () {
    basic.pause(500)
    basic.showArrow(ArrowNames.East)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    basic.showArrow(ArrowNames.West)
})
