def get_input(prompt)
    print prompt
    gets.chomp
  end
  
  def calculate(number1, operator, number2)
    case operator
    when '+'
      number1 + number2
    when '-'
      number1 - number2
    when '*'
      number1 * number2
    when '/'
      number1.to_f / number2
    else
      "Invalid operator"
    end
  end
  
  puts "Welcome to the Ruby Calculator!"
  
  loop do
    num1 = get_input("Enter the first number (or type 'exit' to quit): ").strip
    break if num1.downcase == 'exit'
  
    operator = get_input("Enter operator (+, -, *, /): ").strip
  
    num2 = get_input("Enter the second number: ").strip
    break if num2.downcase == 'exit'
  
    if num1.match(/\A-?\d+\Z/) && num2.match(/\A-?\d+\Z/)
      num1 = num1.to_i
      num2 = num2.to_i
      result = calculate(num1, operator, num2)
      puts "Result: #{result}"
    else
      puts "Invalid input. Please enter numeric values."
    end
  
    puts "-" * 30
  end
  
  puts "Thank you for using the Ruby Calculator!"
  