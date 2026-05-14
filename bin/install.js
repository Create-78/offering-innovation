#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const os = require('os');

const PLUGIN_NAME = 'Offering Innovation';
const DIST_DIR = path.join(__dirname, '..', 'dist', 'claude-code');

function copyRecursive(src, dest) {
  if (!fs.existsSync(src)) return;
  const stat = fs.statSync(src);
  if (stat.isDirectory()) {
    if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
    for (const item of fs.readdirSync(src)) {
      copyRecursive(path.join(src, item), path.join(dest, item));
    }
  } else {
    const destDir = path.dirname(dest);
    if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });
    fs.copyFileSync(src, dest);
  }
}

const args = process.argv.slice(2);
const isGlobal = args.includes('--global') || args.includes('-g');

console.log('');
console.log('  Offering Innovation');
console.log('  ──────────────────────────────────────────────');
console.log('');

if (isGlobal) {
  const claudeDir = path.join(os.homedir(), '.claude');
  copyRecursive(path.join(DIST_DIR, '.claude'), claudeDir);

  console.log('  ✓ Installed globally to ~/.claude/');
  console.log('');
  console.log('  Commands and skills are now available in all Claude Code projects.');
  console.log('');
  console.log('  Note: Global install includes commands and skills only.');
  console.log('  For framework methodology files, use project install: npx offering-innovation-plugin');
  console.log('');
} else {
  const targetDir = process.cwd();

  for (const item of fs.readdirSync(DIST_DIR)) {
    copyRecursive(path.join(DIST_DIR, item), path.join(targetDir, item));
  }

  console.log('  ✓ Installed to ' + targetDir);
  console.log('');
  console.log('  Open Claude Code in this folder and tell Claude your problem:');
  console.log('');
  console.log('    Run Phase 1 on this problem: [your problem statement]');
  console.log('');
  console.log('  Or type /init for guided setup.');
  console.log('');
}
