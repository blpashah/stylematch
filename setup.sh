mkdir -p ~/.streamlit/

echo "\
[server]
headless = true
enableCORS = false
port = 10000
enableXsrfProtection = false
\n\
" > ~/.streamlit/config.toml
