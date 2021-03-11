package main

import (
	"log"
	"time"
	"net/http"
	"encoding/json"
	"github.com/gorilla/mux"
)

func main() {
	router := mux.NewRouter().StrictSlash(true)
    router.HandleFunc("/", Index)

    log.Fatal(http.ListenAndServe(":8000", router))
}

func Index(w http.ResponseWriter, r *http.Request) {
	log.Printf("request at %v\n", time.Now().UTC())

	time.Sleep(2 * time.Second)

	w.Header().Set("Content-Type", "application/json")
	resp := map[string]string{
		"message": "Hello World",
	}
	log.Printf("resp at %v\n", time.Now().UTC())

	json.NewEncoder(w).Encode(resp)
}