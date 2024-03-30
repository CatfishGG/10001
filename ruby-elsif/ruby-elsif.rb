puts "Enter a number:"
number = gets.chomp.to_i

if number < -10000
    puts "You entered a negative number with five or more digits."
elsif number < -1000
    puts "You entered a four digit negative number."
elsif number < -100
    puts "You entered a three digit negative number."
elsif number < -10
    puts "You entered a double digit negative number."
elsif number < 0
    puts "You entered a single digit negative number."
elsif number >= 0 && number < 10
    puts "You entered a single digit positive number."
elsif number >= 10 && number < 100
    puts "You entered a double digit positive number."
elsif number >= 100 && number < 1000
    puts "You entered a three digit positive number."
elsif number >= 1000 && number < 10000
    puts "You entered a four digit positive number."
else
    puts "You entered a positive number with five or more digits."
end