class WordScramble
    def initialize
      @words = [
        "concatenation", "polymorphism", "synchronization", "multithreading",
        "instantiation", "cryptography", "parallelism", "serialization",
        "deprecation", "interpolation", "optimization", "virtualization"
      ]
    end
  
    def scramble_word(word)
      word.chars.shuffle.join
    end
  
    def play
      word = @words.sample
      scrambled_word = scramble_word(word)
  
      puts "Scrambled word: #{scrambled_word}"
      print "Guess the original word: "
  
      guess = gets.chomp
  
      if guess == word
        puts "Congratulations! You guessed correctly."
      else
        puts "Sorry, the correct word was '#{word}'. Better luck next time!"
      end
    end
  end
  
  game = WordScramble.new
  game.play