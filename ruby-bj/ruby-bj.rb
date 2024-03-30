class Card
    attr_reader :rank, :suit
  
    def initialize(rank, suit)
      @rank = rank
      @suit = suit
    end
  
    def value
      return 10 if ['J', 'Q', 'K'].include?(@rank)
      return 11 if @rank == 'A'
      @rank
    end
  
    def to_s
      "#{@rank} of #{@suit}"
    end
  end
  
  class Deck
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  
    def initialize
      @cards = RANKS.product(SUITS).map { |rank, suit| Card.new(rank, suit) }
      shuffle!
    end
  
    def draw
      @cards.pop
    end
  
    private
  
    def shuffle!
      @cards.shuffle!
    end
  end
  
  class Hand
    attr_reader :cards
  
    def initialize
      @cards = []
    end
  
    def add_card(card)
      @cards << card
    end
  
    def value
      total = 0
      aces = 0
      @cards.each do |card|
        total += card.value
        aces += 1 if card.rank == 'A'
      end
  
      while total > 21 && aces > 0
        total -= 10
        aces -= 1
      end
  
      total
    end
  
    def to_s
      @cards.map(&:to_s).join(', ')
    end
  end
  
  class Game
    def initialize
      @deck = Deck.new
      @player_hand = Hand.new
      @dealer_hand = Hand.new
      2.times { @player_hand.add_card(@deck.draw) }
      2.times { @dealer_hand.add_card(@deck.draw) }
    end
  
    def show_hands(final: false)
      puts "Dealer's hand: #{final ? @dealer_hand : @dealer_hand.cards.first}#{final ? '' : ', ??'}"
      puts "Your hand: #{@player_hand} (Total: #{@player_hand.value})"
    end
  
    def player_turn
      loop do
        show_hands
        print "Do you want to (h)it or (s)tand? "
        action = gets.chomp.downcase
        break if action == 's'
  
        if action == 'h'
          @player_hand.add_card(@deck.draw)
          if @player_hand.value > 21
            puts "Your hand: #{@player_hand}"
            puts "Bust! You exceeded 21."
            return :bust
          end
        end
      end
      :stand
    end
  
    def dealer_turn
      while @dealer_hand.value < 17
        @dealer_hand.add_card(@deck.draw)
        if @dealer_hand.value > 21
          show_hands(final: true)
          puts "Dealer busts! You win!"
          return :dealer_bust
        end
      end
      :stand
    end
  
    def compare_hands
      player_value = @player_hand.value
      dealer_value = @dealer_hand.value
  
      show_hands(final: true)
  
      if player_value > dealer_value
        puts "You win!"
      elsif player_value < dealer_value
        puts "Dealer wins!"
      else
        puts "It's a tie!"
      end
    end
  
    def play
      if player_turn != :bust
        if dealer_turn != :dealer_bust
          compare_hands
        end
      end
    end
  end
  
  game = Game.new
  game.play
  