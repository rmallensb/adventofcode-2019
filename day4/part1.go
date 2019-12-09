package main

import "log"
import "math"


func digit(num, place int) int {
    r := num % int(math.Pow10(place))
    return r / int(math.Pow10(place-1))
}

func check(num int) bool {
    double := false

    last := digit(num, 6)
    var now int
    for i:=5; i>0; i-- {
        now = digit(num, i)
        if (last == now) {
            double = true
        }
        if (now < last) {
            return false
        }
        last = now
    }
    return double
}

func main() {
    input_low  := 278888    // 278384
    input_high := 799999    // 824795

    count := 0
/*
    num := input_low
    for i:=1; i<7; i++ {
        last := num
    }
*/
    for num := input_low; num <= input_high; num++ {
        if (check(num)) {
            count++
        }
    }

    log.Println(count)
}
