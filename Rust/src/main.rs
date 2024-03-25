use actix_web::{web, App, HttpResponse, HttpServer};

// Move the index function outside of the main function
async fn index() -> HttpResponse {
    HttpResponse::Ok().body("Hello, world!")
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/", web::get().to(index)) // Now index function can be found
    })
    .bind("127.0.0.1:1337")?
    .run()
    .await
}