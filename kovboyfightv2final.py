from flask import Flask, request, send_file
import random
import time
import threading

app = Flask(__name__)

# Oyun Değişkenleri
player1_ready = False  # Arthur
player2_ready = False  # Aziz
game_started = False
early_click = False
green_time = 0  # Yeşil ışığın yanacağı an (timestamp)
countdown = 5
random_delay = 0  # Rastgele gecikme süresi (ms)
last_countdown_time = 0  # Son geri sayım güncellemesi
winner = ""
reaction_time_global = 0
early_player = ""

# HTML Arayüz (aynı, ama Flask'a uyarla)
main_page = """
<!DOCTYPE html>
<html>
<head>
  <title>Kovboy Duellosu</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { 
      text-align: center; 
      font-family: 'Georgia', serif; 
      background: linear-gradient(135deg, #4b382d, #8b4513); 
      color: #fff;
      margin: 0;
      padding: 20px;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .container { 
      max-width: 500px;
      margin: 0 auto;
      padding: 20px;
      background: rgba(0, 0, 0, 0.4); 
      border-radius: 15px;
      box-shadow: 0 8px 16px rgba(0,0,0,0.5);
    }
    h1 {
      color: #FFD700;
      text-shadow: 3px 3px 6px #000;
      font-size: 2.8em;
      margin-bottom: 25px;
      border-bottom: 2px solid #FFD700;
      padding-bottom: 10px;
    }
    .character { 
      padding: 20px; 
      margin: 15px 0; 
      font-size: 1.2em; 
      font-weight: bold;
      border: 3px solid #FFD700;
      border-radius: 10px; 
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .character:hover {
      transform: translateY(-3px);
      box-shadow: 0 6px 10px rgba(0,0,0,0.5);
    }
    .selected {
      border: 3px solid #00FF00 !important;
      transform: scale(1.03);
    }
    #arthur { 
      background: #556B2F; 
    }
    #aziz { 
      background: #8B0000; 
    }
    #status { 
      font-size: 1.4em; 
      margin: 25px 0;
      padding: 10px;
      background: rgba(255,255,255,0.1);
      border-radius: 8px;
      border: 1px solid #FFD700;
      min-height: 35px;
    }
    #light {
      width: 120px;
      height: 120px;
      border-radius: 50%;
      margin: 20px auto;
      background: #8B0000; 
      border: 5px solid #333;
      box-shadow: 0 0 15px rgba(255,0,0,0.5);
      transition: background 0.3s ease, box-shadow 0.3s ease;
    }
    #fire-button {
      padding: 18px 35px; 
      font-size: 1.3em; 
      font-weight: bold;
      margin: 15px 0; 
      background: #DC143C;
      color: white;
      border: 3px solid #FFD700;
      border-radius: 25px;
      cursor: pointer;
      box-shadow: 0 5px 10px rgba(0,0,0,0.5);
      transition: all 0.2s ease;
      text-transform: uppercase;
    }
    #fire-button:hover {
      background: #FF4500;
    }
    #fire-button:active {
      transform: translateY(2px);
    }
    #result {
      font-size: 1.2em;
      margin: 15px 0;
      padding: 15px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.15);
      min-height: 30px;
    }
    .waiting {
      color: #FFA500;
      animation: pulse 1s infinite;
    }
    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(255, 165, 0, 0.4); }
      70% { box-shadow: 0 0 0 10px rgba(255, 165, 0, 0); }
      100% { box-shadow: 0 0 0 0 rgba(255, 165, 0, 0); }
    }
    .reset-btn {
      margin-top: 20px;
      padding: 10px 20px;
      font-size: 1em;
      background: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background 0.2s;
    }
    .reset-btn:hover {
      background: #0056b3;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>&#x1F920; KOVBOY DUELLOSU &#x1F52B;</h1>
    
    <div id="status">Karakterini Seç Vatansever!</div>
    
    <div id="selection">
      <div class="character" id="arthur" onclick="selectCharacter('arthur')">
        &#x1F920; Arthur Morgan
      </div>
      <div class="character" id="aziz" onclick="selectCharacter('aziz')">
        &#x1F3A9; Aziz Vefa
      </div>
    </div>

    <div id="game" style="display:none">
      <div id="light"></div>
      <button id="fire-button" onclick="fire()" disabled>ATEŞ ET!</button>
    </div>

    <div id="result"></div>
    
    <button id="reset-button" class="reset-btn" onclick="resetGame()" style="display:none;">
        YENİ DÜELLO BAŞLAT
    </button>
    
    <div style="margin-top: 20px; font-size: 0.8em; color: #CCC;">
      PC Kovboy Duellosu v2.0
    </div>
  </div>

  <script>
    let selectedPlayer = '';
    let statusInterval;

    function selectCharacter(player) {
      if(selectedPlayer) {
        document.getElementById(selectedPlayer).classList.remove('selected');
      }
      selectedPlayer = player;
      document.getElementById(selectedPlayer).classList.add('selected');

      document.getElementById("status").innerHTML = "Sunucuya bağlanılıyor...";
      document.getElementById("status").className = "waiting";
      document.getElementById("selection").style.pointerEvents = 'none'; 

      fetch('/select?player=' + player)
        .then(response => response.text())
        .then(data => {
          if (data === "already_selected") {
            document.getElementById("status").innerHTML = "Bu karakter zaten seçilmiş!";
            document.getElementById("status").className = "";
            document.getElementById(selectedPlayer).classList.remove('selected');
            selectedPlayer = '';
            document.getElementById("selection").style.pointerEvents = 'auto';
          } else {
            document.getElementById("selection").style.display = "none";
            startStatusChecking();
          }
        })
        .catch(error => {
          document.getElementById("status").innerHTML = "Bağlantı Hatası!";
          document.getElementById("selection").style.pointerEvents = 'auto';
        });
    }

    function startStatusChecking() {
      if(statusInterval) clearInterval(statusInterval); 
      document.getElementById("game").style.display = "block";
      document.getElementById("reset-button").style.display = "none";

      statusInterval = setInterval(() => {
        fetch('/status?player=' + selectedPlayer)
          .then(response => response.text())
          .then(status => {
            const statusDiv = document.getElementById("status");
            const lightDiv = document.getElementById("light");
            const fireButton = document.getElementById("fire-button");

            if(status.startsWith('waiting')) {
              const waitingFor = status.split(':')[1];
              statusDiv.innerHTML = `&#x23F3; ${waitingFor} bekleniyor... Sabırlı Ol!`;
              statusDiv.className = "waiting";
              lightDiv.style.background = "#8B0000"; 
              lightDiv.style.boxShadow = "0 0 15px rgba(255,0,0,0.5)";
              fireButton.disabled = true;
            } else if(status.startsWith('countdown')) {
              const count = status.split(':')[1];
              statusDiv.innerHTML = `&#x26A1; DÜELLO BAŞLIYOR: ${count} &#x26A1;`;
              statusDiv.className = "";
              lightDiv.style.background = "#FF8C00"; 
              lightDiv.style.boxShadow = "0 0 15px rgba(255,140,0,0.8)";
              fireButton.disabled = true;
            } else if(status === 'prepare') {
              statusDiv.innerHTML = `&#x26A1; HAZIRLAN! &#x26A1;`;
              statusDiv.className = "";
              lightDiv.style.background = "#FF8C00"; 
              lightDiv.style.boxShadow = "0 0 15px rgba(255,140,0,0.8)";
              fireButton.disabled = true;
            } else if(status === 'green') {
              statusDiv.innerHTML = "&#x1F3AF; ATEŞ ET! &#x1F52B;";
              lightDiv.style.background = "#00FF00";
              lightDiv.style.boxShadow = "0 0 30px rgba(0,255,0,1.5)";
              fireButton.disabled = false;
              fireButton.focus(); 
            } else if(status === 'early') {
              handleGameEnd(false, 0); 
            } else if(status === 'opponent_early') {
              handleGameEnd(true, 0, selectedPlayer, 'opponent_early');
            } else if(status.startsWith('win')) {
              const winnerPlayer = status.split(':')[1];
              const reactionTime = parseInt(status.split(':')[2]);
              handleGameEnd(true, reactionTime, winnerPlayer);
            }
          })
          .catch(error => console.error("Status check error:", error));
      }, 100); 
    }

    function fire() {
      document.getElementById("fire-button").disabled = true; 
      
      fetch('/click?player=' + selectedPlayer)
        .then(response => response.text())
        .then(result => {
          if(result.startsWith('win')) {
            const parts = result.split(':');
            const winnerPlayer = parts[1];
            const reactionTime = parseInt(parts[2]);
            handleGameEnd(true, reactionTime, winnerPlayer);
          } else if(result === 'early') {
            handleGameEnd(false, 0);
          } 
        })
        .catch(error => console.error("Fire click error:", error));
    }

    function handleGameEnd(isWin, reactionTime, winnerPlayer = '', reason = '') {
      clearInterval(statusInterval);
      const statusDiv = document.getElementById("status");
      const resultDiv = document.getElementById("result");
      const lightDiv = document.getElementById("light");
      document.getElementById("fire-button").disabled = true;
      document.getElementById("reset-button").style.display = "block";
      
      let resultHTML = '';
      
      if (isWin && winnerPlayer === selectedPlayer) {
          const playerName = selectedPlayer === 'arthur' ? 'Arthur Morgan' : 'Aziz Vefa';
          
          statusDiv.innerHTML = `&#x1F3C6; KAZANAN: ${playerName}! &#x1F3C6;`;
          statusDiv.className = "";
          lightDiv.style.background = "#00FF00"; 
          lightDiv.style.boxShadow = "0 0 30px rgba(0,255,0,1.5)";
          
          if (reason === 'opponent_early') {
            resultHTML = `&#x2705; Rakip yeşil yanmadan ateş etmeye çalıştı, şerif onu yakaladı! Sen kazandın!`;
          } else {
            resultHTML = `&#x2705; Tebrikler! Tepki Süren: **${reactionTime}ms**! En hızlı kovboy sensin!`;
          }
          
      } else if (isWin && winnerPlayer !== selectedPlayer) {
          const loserName = selectedPlayer === 'arthur' ? 'Arthur Morgan' : 'Aziz Vefa';
          const winnerName = winnerPlayer === 'arthur' ? 'Arthur Morgan' : 'Aziz Vefa';
          
          statusDiv.innerHTML = `&#x1F480; KAYBETTİN! &#x1F480;`;
          statusDiv.className = "";
          resultHTML = `Rakibiniz **${winnerName}** sizden daha hızlıydı. Bir sonraki düelloda daha tetikte olun!`;
          lightDiv.style.background = "#FF0000"; 
          lightDiv.style.boxShadow = "0 0 20px rgba(255,0,0,1.5)";
          
      } else if (!isWin) {
          statusDiv.innerHTML = "&#x1F4A5; Şerif seni yakaladı, düzenbaz! &#x1F4A5;";
          statusDiv.className = "";
          resultHTML = "&#x1F52B; Silahına davranamadan seni vurdu. Bir sonraki sefere kurallara uy!";
          lightDiv.style.background = "yellow"; 
          lightDiv.style.boxShadow = "0 0 30px rgba(255,255,0,1.5)";
      }
      
      resultDiv.innerHTML = resultHTML;
      
      if (reactionTime > 0 && reactionTime < 150) {
          resultDiv.innerHTML += "<br><br>&#x1F4AB; **HAYALET!** Bu hız inanılmaz, belki de hile yaptın?";
      }

    }

    function resetGame() {
      document.getElementById("status").innerHTML = "Sıfırlanıyor...";
      document.getElementById("status").className = "";
      
      fetch('/reset')
        .then(response => response.text())
        .then(data => {
          window.location.reload(); 
        })
        .catch(error => {
          document.getElementById("status").innerHTML = "Sıfırlama Hatası!";
        });
    }
  </script>
</body>
</html>
"""

@app.route('/')
def handle_root():
    return main_page

@app.route('/select')
def handle_select():
    global player1_ready, player2_ready, game_started, countdown, last_countdown_time, random_delay, green_time, early_click, winner, reaction_time_global, early_player
    player = request.args.get('player')
    print(f"Oyuncu seçimi: {player}")
    
    if player == "arthur":
        if player1_ready:
            return "already_selected"
        else:
            player1_ready = True
            print("Arthur Morgan hazır")
    elif player == "aziz":
        if player2_ready:
            return "already_selected"
        else:
            player2_ready = True
            print("Aziz Vefa hazır")
    else:
        return "invalid"
    
    if player1_ready and player2_ready and not game_started:
        game_started = True
        countdown = 5
        last_countdown_time = time.time()
        early_click = False
        winner = ""
        reaction_time_global = 0
        early_player = ""
        random_delay = random.randint(2000, 7000) / 1000.0  # saniye cinsine çevir
        green_time = 0  # Geri sayım bitince ayarlanacak
        print("İki oyuncu da hazır - Oyun başlıyor!")
    
    return "OK"

@app.route('/status')
def handle_status():
    global early_click, countdown, green_time, winner, reaction_time_global, early_player
    player = request.args.get('player')
    status = ""
    
    if game_started:
        if early_click:
            if player == early_player:
                status = "early"
            else:
                status = "opponent_early"
        elif countdown > 0:
            status = f"countdown:{countdown}"
        elif time.time() < green_time:
            status = "prepare"
        else:
            status = "green"
    else:
        if early_click:
            if player == early_player:
                status = "early"
            else:
                status = "opponent_early"
        elif winner != "":
            status = f"win:{winner}:{reaction_time_global}"
        else:
            waiting_for = ""
            if not player1_ready and not player2_ready:
                waiting_for = "Her İki Oyuncu"
            elif not player1_ready:
                waiting_for = "Arthur Morgan"
            elif not player2_ready:
                waiting_for = "Aziz Vefa"
            status = f"waiting:{waiting_for}"
    
    return status

@app.route('/click')
def handle_click():
    global game_started, countdown, green_time, early_click, winner, reaction_time_global, early_player
    if not game_started:
        return "not_started"
    
    player = request.args.get('player')
    current_time = time.time()
    
    if countdown > 0 or current_time < green_time:
        early_click = True
        early_player = player
        game_started = False
        print(f"{player} erken davrandı!")
        return "early"
    
    if current_time >= green_time:
        reaction_time = int((current_time - green_time) * 1000)  # ms
        reaction_time_global = reaction_time
        winner = player
        winner_name = "Arthur Morgan" if player == "arthur" else "Aziz Vefa"
        print(f"Kazanan: {winner_name}, Tepki: {reaction_time}ms")
        game_started = False
        return f"win:{player}:{reaction_time}"
    
    return "error"

@app.route('/reset')
def handle_reset():
    global player1_ready, player2_ready, game_started, early_click, countdown, green_time, random_delay, last_countdown_time, winner, reaction_time_global, early_player
    player1_ready = False
    player2_ready = False
    game_started = False
    early_click = False
    countdown = 5
    green_time = 0
    random_delay = 0
    last_countdown_time = 0
    winner = ""
    reaction_time_global = 0
    early_player = ""
    print("Oyun sıfırlandı")
    return "reset"

def countdown_thread():
    global countdown, last_countdown_time, green_time, game_started
    while True:
        if game_started and countdown > 0 and time.time() - last_countdown_time >= 1:
            countdown -= 1
            last_countdown_time = time.time()
            print(f"Countdown: {countdown}")
            if countdown == 0:
                green_time = time.time() + random_delay
                print(f"Yeşil ışık zamanı: {green_time}")
        time.sleep(0.1)

if __name__ == '__main__':
    threading.Thread(target=countdown_thread, daemon=True).start()
    app.run(host='0.0.0.0', port=80, debug=True)