mkdir -p ~/.streamlit/
echo "\
[general]\n\
email=\"21f1001757@student.onlinedegree.iitm.ac.in\"\n
" > ~/.streamlit/config.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
