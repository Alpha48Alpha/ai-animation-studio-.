import { trailerScenes, trailerDuration } from "./data/trailerScenes.js";

export class TrailerPlayer {
  constructor(options = {}) {
    this.scenes = trailerScenes;
    this.duration = trailerDuration;

    this.currentTime = 0;
    this.playing = false;
    this._rafId = null;
    this._lastTimestamp = null;

    this.onTimeUpdate = options.onTimeUpdate || null;
    this.onSceneChange = options.onSceneChange || null;
    this.onStateChange = options.onStateChange || null;
    this.onEnded = options.onEnded || null;

    this._currentScene = null;
  }

  /** Return the scene active at the given time (or null if before/after all scenes). */
  getSceneAt(time) {
    for (const scene of this.scenes) {
      if (time >= scene.start && time < scene.end) {
        return scene;
      }
    }
    return null;
  }

  play() {
    if (this.playing) return;
    if (this.currentTime >= this.duration) {
      this.currentTime = 0;
    }
    this.playing = true;
    this._lastTimestamp = null;
    this._rafId = requestAnimationFrame(this._tick.bind(this));
    this._emitStateChange();
  }

  pause() {
    if (!this.playing) return;
    this.playing = false;
    if (this._rafId !== null) {
      cancelAnimationFrame(this._rafId);
      this._rafId = null;
    }
    this._emitStateChange();
  }

  toggle() {
    if (this.playing) {
      this.pause();
    } else {
      this.play();
    }
  }

  seek(time) {
    this.currentTime = Math.max(0, Math.min(this.duration, time));
    const newScene = this.getSceneAt(this.currentTime);
    if (newScene !== this._currentScene) {
      this._currentScene = newScene;
      this._emitSceneChange(newScene);
    }
    this._emitTimeUpdate();
  }

  /**
   * Core animation loop callback. Called by requestAnimationFrame on each
   * frame: calculates the elapsed delta, advances currentTime, fires scene
   * change and time-update events, and schedules the next frame (or stops
   * playback when the trailer ends).
   */
  _tick(timestamp) {
    if (!this.playing) return;

    if (this._lastTimestamp !== null) {
      const delta = (timestamp - this._lastTimestamp) / 1000;
      this.currentTime = Math.min(this.currentTime + delta, this.duration);
    }
    this._lastTimestamp = timestamp;

    const newScene = this.getSceneAt(this.currentTime);
    if (newScene !== this._currentScene) {
      this._currentScene = newScene;
      this._emitSceneChange(newScene);
    }

    this._emitTimeUpdate();

    if (this.currentTime >= this.duration) {
      this.playing = false;
      this._rafId = null;
      this._emitStateChange();
      if (typeof this.onEnded === "function") this.onEnded();
      return;
    }

    this._rafId = requestAnimationFrame(this._tick.bind(this));
  }

  _emitTimeUpdate() {
    if (typeof this.onTimeUpdate === "function") {
      this.onTimeUpdate(this.currentTime, this.duration);
    }
  }

  _emitSceneChange(scene) {
    if (typeof this.onSceneChange === "function") {
      this.onSceneChange(scene);
    }
  }

  _emitStateChange() {
    if (typeof this.onStateChange === "function") {
      this.onStateChange(this.playing);
    }
  }

  get progress() {
    return this.duration > 0 ? this.currentTime / this.duration : 0;
  }
}
