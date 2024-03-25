package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hello from your Go web server!")
}

func main() {
    http.HandleFunc("/", handler) 
    fmt.Println("Server starting on port 1337")
    http.ListenAndServe(":1337", nil) 
}
