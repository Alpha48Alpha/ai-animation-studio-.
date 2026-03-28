import { TrailerPlayer } from "./player.js";

// ── DOM refs ──────────────────────────────────────────────────────────────
const sceneBg      = document.getElementById("scene-bg");
const sceneText    = document.getElementById("scene-text");
const sceneHeading = document.getElementById("scene-heading");
const sceneMain    = document.getElementById("scene-main");
const sceneSub     = document.getElementById("scene-sub");
const sceneCounter = document.getElementById("scene-counter");
const progressBar  = document.getElementById("progress-bar");
const progressFill = document.getElementById("progress-fill");
const timeDisplay  = document.getElementById("time-display");
const playPauseBtn = document.getElementById("play-pause-btn");
const iconPlay     = document.getElementById("icon-play");
const iconPause    = document.getElementById("icon-pause");
const restartBtn   = document.getElementById("restart-btn");
const muteBtn      = document.getElementById("mute-btn");
const iconSound    = document.getElementById("icon-sound");
const iconMuted    = document.getElementById("icon-muted");
const splash       = document.getElementById("splash");
const playBtnLarge = document.getElementById("play-btn-large");
const audio        = document.getElementById("audio");

// ── Helpers ───────────────────────────────────────────────────────────────
function clamp(value, min, max) { return Math.max(min, Math.min(max, value)); }

function formatTime(secs) {
  const m = Math.floor(secs / 60);
  const s = Math.floor(secs % 60).toString().padStart(2, "0");
  return `${m}:${s}`;
}

let lastBg = "";
function applyScene(scene) {
  if (!scene) {
    sceneHeading.classList.remove("visible");
    sceneMain.classList.remove("visible");
    sceneSub.classList.remove("visible");
    return;
  }

  const newBg = `url('${scene.background}')`;
  if (newBg !== lastBg) {
    lastBg = newBg;
    sceneBg.style.backgroundImage = newBg;
  }

  sceneText.className = `align-${scene.align || "center"}`;

  // Animate text in
  [sceneHeading, sceneMain, sceneSub].forEach(el => el.classList.remove("visible"));
  sceneHeading.textContent = scene.heading || "";
  sceneMain.textContent    = scene.text    || "";
  sceneSub.textContent     = scene.subtext || "";

  // Trigger CSS transitions after a micro-task
  requestAnimationFrame(() => {
    if (scene.heading) sceneHeading.classList.add("visible");
    sceneMain.classList.add("visible");
    if (scene.subtext) sceneSub.classList.add("visible");
  });

  // Counter (e.g. "3 / 9")
  const idx = player.scenes.indexOf(scene) + 1;
  sceneCounter.textContent = `${idx} / ${player.scenes.length}`;
}

function syncPlayIcon(playing) {
  iconPlay.style.display  = playing ? "none"  : "block";
  iconPause.style.display = playing ? "block" : "none";
  playPauseBtn.setAttribute("aria-label", playing ? "Pause" : "Play");
}

function syncAudio(playing, currentTime) {
  if (playing) {
    audio.currentTime = currentTime;
    audio.play().catch(() => {});
  } else {
    audio.pause();
  }
}

// Track whether playback has reached the end (used by the splash replay logic)
let hasEnded = false;

// ── Player ────────────────────────────────────────────────────────────────
const player = new TrailerPlayer({
  onTimeUpdate(time, duration) {
    const pct = duration > 0 ? (time / duration) * 100 : 0;
    progressFill.style.width = `${pct}%`;
    progressBar.setAttribute("aria-valuenow", Math.round(pct));
    timeDisplay.textContent = `${formatTime(time)} / ${formatTime(duration)}`;
  },

  onSceneChange(scene) {
    applyScene(scene);
  },

  onStateChange(playing) {
    syncPlayIcon(playing);
    syncAudio(playing, player.currentTime);
  },

  onEnded() {
    hasEnded = true;
    syncPlayIcon(false);
    audio.pause();
    // Show replay splash
    splash.querySelector("#splash-sub").textContent = "Replay";
    splash.classList.remove("hidden");
  },
});

// Show the first scene as background on load
applyScene(player.scenes[0]);
sceneBg.style.backgroundImage = `url('${player.scenes[0].background}')`;
sceneCounter.textContent = `1 / ${player.scenes.length}`;

// ── UI events ─────────────────────────────────────────────────────────────
playBtnLarge.addEventListener("click", () => {
  splash.classList.add("hidden");
  if (hasEnded) {
    hasEnded = false;
    player.seek(0);
  }
  player.play();
});

playPauseBtn.addEventListener("click", () => {
  if (!splash.classList.contains("hidden")) {
    splash.classList.add("hidden");
  }
  player.toggle();
});

restartBtn.addEventListener("click", () => {
  player.seek(0);
  applyScene(player.scenes[0]);
  if (!player.playing) player.play();
});

muteBtn.addEventListener("click", () => {
  audio.muted = !audio.muted;
  iconSound.style.display = audio.muted ? "none"  : "block";
  iconMuted.style.display = audio.muted ? "block" : "none";
  muteBtn.setAttribute("aria-label", audio.muted ? "Unmute" : "Mute");
});

// Progress bar — click to seek
progressBar.addEventListener("click", (e) => {
  const rect = progressBar.getBoundingClientRect();
  const ratio = clamp((e.clientX - rect.left) / rect.width, 0, 1);
  player.seek(ratio * player.duration);
  if (!player.playing) {
    audio.currentTime = player.currentTime;
  }
});

// Progress bar — keyboard seek (← →)
progressBar.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight") player.seek(player.currentTime + 2);
  if (e.key === "ArrowLeft")  player.seek(player.currentTime - 2);
});

// Space bar — toggle play/pause
document.addEventListener("keydown", (e) => {
  if (e.target.tagName === "BUTTON" || e.target.tagName === "INPUT") return;
  if (e.code === "Space") {
    e.preventDefault();
    if (!splash.classList.contains("hidden")) {
      splash.classList.add("hidden");
      player.play();
    } else {
      player.toggle();
    }
  }
});

// ── Idle hide controls ────────────────────────────────────────────────────
let idleTimer = null;
function resetIdle() {
  document.body.classList.remove("idle");
  clearTimeout(idleTimer);
  if (player.playing) {
    idleTimer = setTimeout(() => document.body.classList.add("idle"), 3500);
  }
}
document.addEventListener("mousemove", resetIdle);
document.addEventListener("keydown",   resetIdle);
document.addEventListener("click",     resetIdle);
