package main

import "log"
import "math"


func digit(num, place int) int {
    r := num % int(math.Pow10(place))
    return r / int(math.Pow10(place-1))
}

func check(num int) bool {
    double := false
    Double := false             // to store early doubles like 112222
    current_double := false

    last := digit(num, 6)
    var now int
    for i:=5; i>0; i-- {
        now = digit(num, i)

        if (last == now) {
            double = true

            if current_double {
                double = false
            } else {
                current_double = true
            }
        } else {
            current_double = false
            if (double) {
                Double = true
            }
        }
        if (now < last) {
            return false
        }
        last = now
    }
    return (double || Double)
}

func main() {
    input_low  := 278888    // 278384
    input_high := 799999    // 824795

    log.Println(check(112222))

    count := 0
    for num := input_low; num <= input_high; num++ {
        if (check(num)) {
            count++
        }
    }

    log.Println(count)
}
