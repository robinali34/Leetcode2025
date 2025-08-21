#!/usr/bin/env python3
"""
LeetCode Progress Tracker

This script helps track your progress through LeetCode problems,
including completion status, difficulty levels, and performance metrics.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class ProblemStatus:
    """Represents the status of a LeetCode problem."""
    problem_id: str
    title: str
    difficulty: str
    category: str
    completed: bool
    completed_date: Optional[str]
    language: str  # 'cpp', 'python', or 'both'
    time_taken: Optional[int]  # in minutes
    notes: str
    rating: Optional[int]  # 1-5 rating of difficulty
    tags: List[str]


class ProgressTracker:
    """Main class for tracking LeetCode progress."""
    
    def __init__(self, data_file: str = "progress/problems.json"):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.problems: Dict[str, ProblemStatus] = {}
        self.load_progress()
    
    def load_progress(self):
        """Load progress from JSON file."""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for problem_data in data.values():
                        problem = ProblemStatus(**problem_data)
                        self.problems[problem.problem_id] = problem
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error loading progress: {e}")
                self.problems = {}
        else:
            self.problems = {}
    
    def save_progress(self):
        """Save progress to JSON file."""
        data = {pid: asdict(problem) for pid, problem in self.problems.items()}
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_problem(self, problem_id: str, title: str, difficulty: str, 
                   category: str = "Array", tags: Optional[List[str]] = None):
        """Add a new problem to track."""
        if problem_id not in self.problems:
            self.problems[problem_id] = ProblemStatus(
                problem_id=problem_id,
                title=title,
                difficulty=difficulty,
                category=category,
                completed=False,
                completed_date=None,
                language="",
                time_taken=None,
                notes="",
                rating=None,
                tags=tags or []
            )
            self.save_progress()
            print(f"Added problem {problem_id}: {title}")
        else:
            print(f"Problem {problem_id} already exists")
    
    def mark_completed(self, problem_id: str, language: str, 
                      time_taken: Optional[int] = None, notes: str = ""):
        """Mark a problem as completed."""
        if problem_id in self.problems:
            problem = self.problems[problem_id]
            problem.completed = True
            problem.completed_date = datetime.now().isoformat()
            problem.language = language
            problem.time_taken = time_taken
            problem.notes = notes
            self.save_progress()
            print(f"Marked problem {problem_id} as completed in {language}")
        else:
            print(f"Problem {problem_id} not found")
    
    def update_rating(self, problem_id: str, rating: int):
        """Update difficulty rating for a problem."""
        if problem_id in self.problems and 1 <= rating <= 5:
            self.problems[problem_id].rating = rating
            self.save_progress()
            print(f"Updated rating for problem {problem_id} to {rating}")
        else:
            print(f"Invalid problem ID or rating")
    
    def get_progress_summary(self) -> Dict:
        """Get a summary of progress statistics."""
        total = len(self.problems)
        completed = sum(1 for p in self.problems.values() if p.completed)
        by_difficulty = {}
        by_language = {"cpp": 0, "python": 0, "both": 0}
        
        for problem in self.problems.values():
            if problem.completed:
                by_difficulty[problem.difficulty] = by_difficulty.get(problem.difficulty, 0) + 1
                by_language[problem.language] += 1
        
        return {
            "total_problems": total,
            "completed": completed,
            "completion_rate": (completed / total * 100) if total > 0 else 0,
            "by_difficulty": by_difficulty,
            "by_language": by_language
        }
    
    def print_progress(self):
        """Print current progress to console."""
        summary = self.get_progress_summary()
        
        print("\n" + "="*50)
        print("LEETCODE PROGRESS SUMMARY")
        print("="*50)
        print(f"Total Problems: {summary['total_problems']}")
        print(f"Completed: {summary['completed']}")
        print(f"Completion Rate: {summary['completion_rate']:.1f}%")
        
        print("\nBy Difficulty:")
        for diff, count in summary['by_difficulty'].items():
            print(f"  {diff.capitalize()}: {count}")
        
        print("\nBy Language:")
        for lang, count in summary['by_language'].items():
            if count > 0:
                print(f"  {lang.upper()}: {count}")
        
        print("\nRecent Completions:")
        recent = sorted(
            [p for p in self.problems.values() if p.completed],
            key=lambda x: x.completed_date or "",
            reverse=True
        )[:5]
        
        for problem in recent:
            print(f"  {problem.problem_id}: {problem.title} ({problem.language})")
        
        print("="*50)
    
    def export_to_csv(self, filename: str = "progress/leetcode_progress.csv"):
        """Export progress to CSV format."""
        import csv
        
        csv_file = Path(filename)
        csv_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Problem ID', 'Title', 'Difficulty', 'Category', 'Completed',
                'Completed Date', 'Language', 'Time Taken', 'Rating', 'Tags', 'Notes'
            ])
            
            for problem in self.problems.values():
                writer.writerow([
                    problem.problem_id, problem.title, problem.difficulty,
                    problem.category, problem.completed, problem.completed_date,
                    problem.language, problem.time_taken, problem.rating,
                    ', '.join(problem.tags), problem.notes
                ])
        
        print(f"Progress exported to {csv_file}")


def main():
    """Main function to demonstrate the progress tracker."""
    tracker = ProgressTracker()
    
    # Example usage
    if not tracker.problems:
        print("Adding sample problems...")
        tracker.add_problem("1", "Two Sum", "Easy", "Array", ["Hash Table", "Array"])
        tracker.add_problem("2", "Add Two Numbers", "Medium", "Linked List", ["Linked List", "Math"])
        tracker.add_problem("3", "Longest Substring Without Repeating Characters", "Medium", "String", ["Hash Table", "String", "Sliding Window"])
    
    # Mark some as completed
    tracker.mark_completed("1", "python", 15, "Used hash table approach")
    tracker.mark_completed("2", "cpp", 25, "Linked list manipulation")
    
    # Update ratings
    tracker.update_rating("1", 2)
    tracker.update_rating("2", 4)
    
    # Print progress
    tracker.print_progress()
    
    # Export to CSV
    tracker.export_to_csv()


if __name__ == "__main__":
    main() 