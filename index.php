<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

class ViewerBot {
    private $url;
    private $referrers = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.reddit.com",
    "https://www.linkedin.com",
    "http://google.com.sg",
    "http://google.co.id",
    "http://google.com.my",
    "http://google.jp",
    "http://google.us",
    "http://google.tl",
    "http://google.ac",
    "http://google.ad",
    "http://google.ae",
    "http://google.af",
    "http://google.ag",
    "http://google.ru",
    "http://google.by",
    "http://google.ca",
    "http://google.cn",
    "http://google.cl",
    "http://google.cm",
    "http://google.cv",
    "http://google.gg",
    "http://google.ge",
    "http://google.gr",
    "http://google.com.tw",
    "https://search.yahoo.com",
    "http://www.beinyu.com"
];
    
    private $userAgents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
    ];
    
    public function __construct($url) {
        $this->url = $url;
    }
    
    public function visit() {
        try {
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, $this->url);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
            curl_setopt($ch, CURLOPT_USERAGENT, $this->userAgents[array_rand($this->userAgents)]);
            curl_setopt($ch, CURLOPT_REFERER, $this->referrers[array_rand($this->referrers)]);
            curl_setopt($ch, CURLOPT_TIMEOUT, 10);
            
            $result = curl_exec($ch);
            $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
            $error = curl_error($ch);
            curl_close($ch);


            usleep(200000); 
            
            return [
                "success" => ($httpCode >= 200 && $httpCode < 300),
                "code" => $httpCode,
                "error" => $error,
                "referer" => $this->referrers[array_rand($this->referrers)]
            ];
        } catch (Exception $e) {
            return [
                "success" => false,
                "code" => 0,
                "error" => $e->getMessage(),
                "referer" => "N/A"
            ];
        }
    }
}


if (isset($_GET['ajax']) && isset($_GET['url']) && isset($_GET['current'])) {
    header('Content-Type: application/json');
    $bot = new ViewerBot($_GET['url']);
    $result = $bot->visit();
    echo json_encode($result);
    exit;
}

$error = '';
if (isset($_GET['url']) && !filter_var($_GET['url'], FILTER_VALIDATE_URL)) {
    $error = "Invalid URL format";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>MATA - Wanz Xploit</title>
    <style>
        :root {
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --success: #22c55e;
            --error: #ef4444;
            --background: #0f172a;
            --surface: #1e293b;
            --surface-light: #334155;
            --text: #f1f5f9;
            --text-secondary: #94a3b8;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, sans-serif;
        }

        body {
            background-color: var(--background);
            color: var(--text);
            line-height: 1.6;
            padding: 16px;
            min-height: 100vh;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        
        .container {
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            padding: 0 env(safe-area-inset-right) 0 env(safe-area-inset-left); 
        }

        h1 {
            text-align: center;
            color: var(--primary);
            margin: 20px 0 30px;
            font-size: clamp(1.5rem, 5vw, 2.5rem); 
            text-shadow: 0 0 20px rgba(99, 102, 241, 0.2);
            padding: 0 10px;
            line-height: 1.2;
        }

        .card {
            background-color: var(--surface);
            padding: clamp(16px, 4vw, 25px);
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            margin-bottom: 20px;
            border: 1px solid var(--surface-light);
            overflow: hidden; 
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: var(--text-secondary);
            font-size: 0.95em;
            font-weight: 500;
        }

        
        input {
            width: 100%;
            padding: 14px 16px;
            background-color: var(--surface-light);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text);
            border-radius: 8px;
            font-size: 16px; 
            transition: all 0.3s ease;
            -webkit-appearance: none; 
            appearance: none;
        }

        input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
        }

        
        input[type="number"] {
            font-size: 16px;
        }

        
        button {
            width: 100%;
            padding: 16px;
            background-color: var(--primary);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            touch-action: manipulation;
            -webkit-appearance: none;
            appearance: none;
        }

        button:active {
            transform: scale(0.98);
        }

        button:disabled {
            opacity: 0.7;
            cursor: not-allowed;
        }

        .progress {
            margin-top: 20px;
            background-color: var(--surface-light);
            border-radius: 8px;
            height: 8px; 
            overflow: hidden;
        }

        .progress-bar {
            height: 100%;
            background-color: var(--primary);
            transition: width 0.3s ease;
        }

        .results {
            margin-top: 30px;
            padding-bottom: env(safe-area-inset-bottom); 
        }

        .result-item {
            padding: 16px;
            margin-bottom: 12px;
            border-radius: 8px;
            background-color: var(--surface-light);
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            display: flex;
            flex-direction: column; 
            gap: 8px;
        }

        @media (min-width: 640px) {
            .result-item {
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
            }
        }

        .result-item.show {
            opacity: 1;
            transform: translateY(0);
        }

        .result-item.success {
            border-left: 4px solid var(--success);
        }

        .result-item.error {
            border-left: 4px solid var(--error);
        }

        .result-info {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .visit-number {
            font-weight: 500;
            font-size: 0.95em;
        }

        .referer {
            font-size: 0.85em;
            color: var(--text-secondary);
            word-break: break-all; 
        }

        .status-badge {
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.85em;
            font-weight: 600;
            white-space: nowrap;
            align-self: flex-start; 
        }

        @media (min-width: 640px) {
            .status-badge {
                align-self: center;
            }
        }

        .status-badge.success {
            background-color: rgba(34, 197, 94, 0.2);
            color: #4ade80;
        }

        .status-badge.error {
            background-color: rgba(239, 68, 68, 0.2);
            color: #f87171;
        }

        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }

        .loading {
            animation: pulse 1.5s infinite;
        }

        
        html {
            scroll-behavior: smooth;
        }

        
        @media (hover: hover) {
            button:hover {
                background-color: var(--primary-dark);
                transform: translateY(-1px);
            }
        }

        
        @media (prefers-color-scheme: dark) {
            
        }

        
        body {
            overscroll-behavior-y: contain;
        }

        
        @supports (-webkit-touch-callout: none) {
            body {
                cursor: default;
            }
            
            input, button {
                cursor: pointer;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>MATA Web View Server</h1>
        
        <div class="card">
            <form id="viewerForm" method="GET">
                <div class="form-group">
                    <label>Target URL</label>
                    <input type="url" name="url" placeholder="https://example.com" 
                           value="<?php echo isset($_GET['url']) ? htmlspecialchars($_GET['url']) : ''; ?>"
                           autocomplete="off" required>
                </div>
                <div class="form-group">
                    <label>Number of Views (1-1000)</label>
                    <input type="number" name="max" placeholder="Enter number of views" 
                           value="<?php echo isset($_GET['max']) ? htmlspecialchars($_GET['max']) : '100'; ?>"
                           min="1" max="1000" required>
                </div>
                <button type="submit" id="submitBtn">Generate Views</button>
            </form>

            <?php if (isset($_GET['url']) && isset($_GET['max'])): ?>
            <div class="progress">
                <div class="progress-bar" id="progressBar" style="width: 0%"></div>
            </div>
            <?php endif; ?>
        </div>

        <?php if ($error): ?>
            <div class="card error">
                <?php echo htmlspecialchars($error); ?>
            </div>
        <?php endif; ?>

        <div id="results" class="results"></div>
    </div>

    <script>
        const form = document.getElementById('viewerForm');
        const results = document.getElementById('results');
        const submitBtn = document.getElementById('submitBtn');
        const progressBar = document.getElementById('progressBar');
        
        async function processViews(url, max) {
            submitBtn.disabled = true;
            results.innerHTML = '';
            let current = 0;
            
            while (current < max) {
                try {
                    const response = await fetch(`?ajax=1&url=${encodeURIComponent(url)}&current=${current}`);
                    const result = await response.json();
                    
                    const resultItem = document.createElement('div');
                    resultItem.className = `result-item ${result.success ? 'success' : 'error'}`;
                    
                    resultItem.innerHTML = `
                        <div class="result-info">
                            <span class="visit-number">Visit #${current + 1}</span>
                            <div class="referer">From: ${result.referer}</div>
                        </div>
                        <span class="status-badge ${result.success ? 'success' : 'error'}">
                            ${result.success ? 'Success' : 'Failed'} (${result.code})
                        </span>
                    `;
                    
                    results.appendChild(resultItem);
                    setTimeout(() => resultItem.classList.add('show'), 50);
                    
                    current++;
                    progressBar.style.width = `${(current / max) * 100}%`;
                    
                    resultItem.scrollIntoView({ behavior: 'smooth', block: 'end' });
                } catch (error) {
                    console.error('Error:', error);
                }
            }
            
            submitBtn.disabled = false;
        }
        
        if (form) {
            const urlParam = new URLSearchParams(window.location.search).get('url');
            const maxParam = new URLSearchParams(window.location.search).get('max');
            
            if (urlParam && maxParam) {
                processViews(urlParam, parseInt(maxParam));
            }
        }
    </script>
</body>
</html>