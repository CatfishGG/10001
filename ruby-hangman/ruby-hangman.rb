class Hangman
    attr_reader :word, :guesses, :max_attempts, :attempted_letters
  
    def initialize(word_list, max_attempts = 7)
      @word = word_list.sample.upcase
      @guesses = "_" * @word.length
      @max_attempts = max_attempts
      @attempted_letters = []
    end
  
    def guess(letter)
      letter.upcase!
      return if @attempted_letters.include?(letter)
      
      @attempted_letters << letter
      if word.include?(letter)
        update_guesses(letter)
      else
        @max_attempts -= 1
      end
    end
  
    def update_guesses(letter)
      word.chars.each_with_index do |char, index|
        if char == letter
          @guesses[index] = letter
        end
      end
    end
  
    def game_over?
      @max_attempts.zero? || @guesses == @word
    end
  
    def display_status
      puts "Word: #{@guesses}"
      puts "Attempts remaining: #{@max_attempts}"
      puts "Attempted letters: #{@attempted_letters.sort.join}"
    end
  
    def play
      until game_over?
        display_status
        print "Please guess a letter: "
        guess(gets.chomp)
      end
  
      puts "Game over! The word was '#{@word}'."
      if @guesses == @word
        puts "Congratulations! You've guessed the word!"
      else
        puts "Better luck next time!"
      end
    end
  end
  
  word_list = ["hangman", "ruby", "programming", "terminal", "puzzle", "challenge"]
  game = Hangman.new(word_list)
  game.play