puts "Enter a number:"
number = gets.chomp.to_i

if number % 2 == 0
    puts "You entered an even number."
else
    puts "You entered an odd number."
end