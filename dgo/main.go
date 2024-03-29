package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/bwmarrin/discordgo"
)

func main() {
	discord, err := discordgo.New("Bot " + os.Getenv("TOKEN"))
	if err != nil {
		fmt.Println("error creating Discord session,", err)
		return
	}

	discord.AddHandler(messageCreate)

	err = discord.Open()
	if err != nil {
		fmt.Println("error opening connection,", err)
		return
	}

	fmt.Println("Bot is now running. Press CTRL-C to exit.")
	sc := make(chan os.Signal, 1)
	signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt)
	<-sc

	discord.Close()
}


func messageCreate(s *discordgo.Session, m *discordgo.MessageCreate) {
	if m.Author.ID == s.State.User.ID {
		return
	}

	if m.Content == "bhej" {
		files := []string{"kali-linux.png", "parac.png", "Z.png"}

		for _, fileName := range files {
			file, err := os.Open(fileName)
			if err != nil {
				fmt.Println("error opening file,", err)
				continue
			}

			_, err = s.ChannelFileSend(m.ChannelID, fileName, file)
			file.Close()
			if err != nil {
				fmt.Println("error sending file,", err)
				continue
			}

			time.Sleep(30 * time.Second)
		}
	}
}